""" User Income Set Request Definition """
from rowantree.common.sdk import BaseModel
from rowantree.contracts import StoreType


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

    income_source_name: StoreType
    amount: int
