""" Active Feature Response Definition """

from pydantic import BaseModel

from rowantree.contracts import FeatureType


class ActiveFeatureResponse(BaseModel):
    """
    Active Feature Response DTO

    Attributes
    ----------
    active_feature: FeatureType
        The current active feature of the user.
    """

    active_feature: FeatureType
