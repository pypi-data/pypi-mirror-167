""" UserIncomeGetResponse Definition """

from rowantree.common.sdk import BaseModel
from rowantree.contracts import StoreType, UserIncome


class UserIncomeGetResponse(BaseModel):
    """
    UserIncomeGetResponse DTO
    A dictionary of user incomes, keyed by income name.
    """

    incomes: dict[StoreType, UserIncome]
