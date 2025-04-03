from enum import Enum


class User(str, Enum):
    START_USER_DATA_STREAM = "/api/v3/userDataStream" # post, start new user data stream. closes after 60 min unless a keepalive is sent
    KEEPALIVE_USER_DATA_STREAM = "/api/v3/userDataStream" # put, keepalive user data stream to prevent timeout, recommended to send a ping every 30 min
    CLOSE_USER_DATA_STREAM = "/api/v3/userDataStream" # delete, close out a user data stream
    
    
    def __str__(self) -> str:
        return self.value
