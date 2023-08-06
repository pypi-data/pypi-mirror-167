""" UserIncomeGetResponse Definition """

from rowantree.contracts import BaseModel, StoreType, UserStore


class UserIncomeGetResponse(BaseModel):
    """
    UserIncomeGetResponse DTO
    A dictionary of user incomes, keyed by income name.
    """

    incomes: dict[StoreType, UserStore]
