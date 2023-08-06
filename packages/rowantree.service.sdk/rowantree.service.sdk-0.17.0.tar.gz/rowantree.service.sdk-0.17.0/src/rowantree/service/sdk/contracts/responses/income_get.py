""" UserIncomeGetResponse Definition """

from rowantree.contracts import BaseModel, StoreType, UserIncome


class UserIncomeGetResponse(BaseModel):
    """
    UserIncomeGetResponse DTO
    A dictionary of user incomes, keyed by income name.
    """

    incomes: dict[StoreType, UserIncome]
