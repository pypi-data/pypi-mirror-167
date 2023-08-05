""" User Transport Request Definition """

from pydantic import BaseModel


class UserTransportRequest(BaseModel):
    """
    User Transport Request DTO

    NOTE/TODO:
        We've mixed location and feature.  We need to refactor location -> feature.

    Attributes
    ----------
    location: str
        The name of the feature (location).
    """

    location: str
