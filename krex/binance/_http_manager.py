import requests
from dataclasses import dataclass, field


@dataclass
class HTTPManager:
    api_key: str = field(default=None)
    api_secret: str = field(default=None)
    session: requests.Session = field(default_factory=requests.Session, init=False)

    def _request(self, method, path, query=None):
        pass
