""" MerchantTransformsGetResponse Definition """

from rowantree.common.sdk import BaseModel
from rowantree.contracts import StoreType


class MerchantTransformsGetResponse(BaseModel):
    """
    MerchantTransformsGetResponse DTO
    The (unique) set of user merchants.
    """

    merchants: set[StoreType]
