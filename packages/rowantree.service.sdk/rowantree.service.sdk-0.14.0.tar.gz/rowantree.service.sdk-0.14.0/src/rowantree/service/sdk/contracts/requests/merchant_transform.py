""" Merchant Transform Request Definition """

from pydantic import BaseModel


class MerchantTransformRequest(BaseModel):
    """
    Merchant Transform Request DTO

    Attributes
    ----------
    store_name: str
        The name of the store to transform.
    """

    store_name: str
