""" StoresGetResponse Definition """

from pydantic import BaseModel

from rowantree.contracts import StoreType, UserStore


class StoresGetResponse(BaseModel):
    """
    StoresGetResponse DTO

    Attributes
    ----------
    stores: dict[StoreType, UserStore]
        A dictionary of user stores, keyed by store name.
    """

    stores: dict[StoreType, UserStore]
