import logging
import json
import httpx
import msgpack
from dataclasses import dataclass, field
from eth_account import Account
from eth_account.messages import encode_typed_data
from eth_utils import keccak, to_hex
from ..product_table.manager import ProductTableManager
from ...utils.errors import FailedRequestError
from ...utils.helpers import generate_timestamp
from ...utils.address_utils import address_to_bytes
from ...utils.common import Common

HTTP_URL = "https://{SUBDOMAIN}.{DOMAIN}.{TLD}"
SUBDOMAIN_MAIN = "api"
DOMAIN_MAINNET = "hyperliquid"
DOMAIN_TESTNET = "hyperliquid-testnet"
TLD_MAIN = "xyz"
contract_address = {
    "Mainnet": {
        "chainId": 42161,
        "verifyingContract": "0xYourExchangeContractAddress",  # 替换成文档里给的地址
    },
    "Testnet": {
        "chainId": 421613,
        "verifyingContract": "0xYourExchangeContractAddress",  # 替换成文档里给的地址
    },
}


def get_header():
    return {"Content-Type": "application/json"}


@dataclass
class HTTPManager:
    testnet: bool = field(default=False)
    subdomain: str = field(default=SUBDOMAIN_MAIN)
    tld: str = field(default=TLD_MAIN)
    wallet_address: str = field(default=None)
    private_key: str = field(default=None)
    timeout: int = field(default=10)
    recv_window: int = field(default=5000)
    max_retries: int = field(default=3)
    retry_delay: int = field(default=3)
    logger: logging.Logger = field(default=None)
    session: httpx.AsyncClient = field(init=False)
    ptm: ProductTableManager = field(init=False)
    preload_product_table: bool = field(default=True)

    async def async_init(self):
        self.session = httpx.AsyncClient(timeout=self.timeout)
        self._logger = self.logger or logging.getLogger(__name__)
        if self.preload_product_table:
            self.ptm = await ProductTableManager.get_instance(Common.HYPERLIQUID)
        domain = DOMAIN_TESTNET if self.testnet else DOMAIN_MAINNET
        self.endpoint = HTTP_URL.format(SUBDOMAIN=self.subdomain, DOMAIN=domain, TLD=self.tld)
        return self

    def _auth(self, query, timestamp):
        wallet = Account.from_key(self.private_key)
        data = msgpack.packb(query["action"])
        data += timestamp.to_bytes(8, "big")

        if query.get("vaultAddress"):
            data += b"\x01"
            data += address_to_bytes(query["vaultAddress"])
        else:
            data += b"\x00"
        if query.get("expireAfter"):
            data += b"\x00"
            data += query["expireAfter"].to_bytes(8, "big")
        hash = keccak(data)
        phantom_agent = {"source": "b" if self.testnet else "a", "connectionId": hash}

        data = {
            "domain": {
                "chainId": 1337,
                "name": "Exchange",
                "verifyingContract": "0x0000000000000000000000000000000000000000",
                "version": "1",
            },
            "types": {
                "Agent": [
                    {"name": "source", "type": "string"},
                    {"name": "connectionId", "type": "bytes32"},
                ],
                "EIP712Domain": [
                    {"name": "name", "type": "string"},
                    {"name": "version", "type": "string"},
                    {"name": "chainId", "type": "uint256"},
                    {"name": "verifyingContract", "type": "address"},
                ],
            },
            "primaryType": "Agent",
            "message": phantom_agent,
        }

        encoded = encode_typed_data(full_message=data)
        signed = wallet.sign_message(encoded)

        return {"r": to_hex(signed["r"]), "s": to_hex(signed["s"]), "v": signed["v"]}

    async def _request(
        self,
        method: str,
        path: str,
        query: dict = None,
        signed: bool = True,
    ):
        if not self.session:
            await self.async_init()

        if query is None:
            query = {}

        timestamp = generate_timestamp()

        if method.upper() == "GET":
            if query:
                sorted_query = "&".join(f"{k}={v}" for k, v in sorted(query.items()) if v)
                path += "?" + sorted_query if sorted_query else ""
                payload = sorted_query
            else:
                payload = ""
        else:
            payload = json.dumps(query, separators=(",", ":"), ensure_ascii=False)

        if signed:
            if not (self.wallet_address and self.private_key):
                raise ValueError("Signed request requires Address and Private Key of wallet.")
            query["nonce"] = timestamp
            query["signature"] = self._auth(query, timestamp)

        headers = get_header()

        url = self.endpoint + path

        try:
            if method.upper() == "GET":
                response = await self.session.get(url, headers=headers)
            elif method.upper() == "POST":
                response = await self.session.post(url, headers=headers, json=query if query else {})
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            try:
                data = response.json()
            except Exception:
                data = {}

            if not response.status_code // 100 == 2:
                raise FailedRequestError(
                    request=f"{method.upper()} {url} | Body: {query}",
                    message=f"HTTP Error {response.status_code}: {response.text}",
                    status_code=response.status_code,
                    time=timestamp,
                    resp_headers=response.headers,
                )

            return data

        except httpx.HTTPError as e:
            raise FailedRequestError(
                request=f"{method.upper()} {url} | Body: {payload}",
                message=f"Request failed: {str(e)}",
                status_code=getattr(e.response, "status_code", "Unknown"),
                time=timestamp,
                resp_headers=getattr(e.response, "headers", None),
            )
