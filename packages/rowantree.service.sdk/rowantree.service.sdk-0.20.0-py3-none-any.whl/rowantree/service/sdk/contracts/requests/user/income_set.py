""" User Income Set Request Definition """
from rowantree.contracts import BaseModel, StoreType


class UserIncomeSetRequest(BaseModel):
    """
    User Income Set Request DTO.

    Attributes
    ----------
    income_source_name: StoreType
        The income source name (worker type)
    amount: int
        The amount to set for the specified type. (As an absolute)
    """

    user_guid: str
    income_source_name: StoreType
    amount: int
