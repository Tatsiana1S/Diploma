from enum import Enum


class Status(Enum):
    """
    This is all pet statuses
    """
    Available: str = "available"
    Pending: str = "pending"
    Sold: str = "sold"


class HttpStatusCode(Enum):
    """
    This is HTTP status codes
    """
    OK: int = 200
    BadRequest: int = 400
    NotFound: int = 404
