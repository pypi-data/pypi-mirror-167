""" User Income Set Request Definition """
from pydantic import BaseModel


class UserIncomeSetRequest(BaseModel):
    """
    User Income Set Request DTO.

    Attributes
    ----------
    income_source_name: str
        The income source name (worker type)
    amount: int
        The amount to set for the specified type. (As an absolute)
    """

    income_source_name: str
    amount: int
