""" Merchant Transform Request Definition """

from pydantic import BaseModel

from rowantree.contracts import StoreType


class MerchantTransformRequest(BaseModel):
    """
    Merchant Transform Request DTO

    Attributes
    ----------
    store_name: StoreType
        The name of the store to transform.
    """

    store_name: StoreType
