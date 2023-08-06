""" User Active Definition """
from rowantree.common.sdk import BaseModel


class UserActiveGetStatus(BaseModel):
    """
    UserActiveGetStatus DTO
    Defines the user active state.

    Attributes
    ----------
    active: bool
        The user active state.
    """

    active: bool
