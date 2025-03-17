# from krex.bitmart.client import Client
# from krex.utils.errors import APIException
# from krex.utils.helpers import config_logging
# import logging

# config_logging(logging, logging.DEBUG)
# logger = logging.getLogger(__name__)

# BITMART_API_KEY = "api_key"
# BITMART_API_SECRET = "api_secret"
# MEMO = "memo"

# client = Client(
#     api_key=BITMART_API_KEY,
#     api_secret=BITMART_API_SECRET,
#     memo=MEMO,
#     logger=logger,
# )

# try:
#     response = client.get_funding_rate_history(symbol="BTCUSDT")
#     logger.info(response)
# except APIException as error:
#     logger.error(
#         "Found error. status: {}, error message: {}".format(
#             error.status_code, error.response
#         )
#     )

from krex.bitmart.client import Client

BITMART_API_KEY = "api_key"
BITMART_API_SECRET = "api_secret"
MEMO = "memo"

client = Client(
    api_key=BITMART_API_KEY,
    api_secret=BITMART_API_SECRET,
    memo=MEMO,
)

response = client.get_funding_rate_history(symbol="BTCUSDT")
print(response)
