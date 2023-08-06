""" User Transport Request Definition """

from rowantree.common.sdk import BaseModel
from rowantree.contracts import FeatureType


class UserTransportRequest(BaseModel):
    """
    User Transport Request DTO

    NOTE/TODO:
        We've mixed location and feature.  We need to refactor location -> feature.

    Attributes
    ----------
    location: FeatureType
        The name of the feature (location).
    """

    location: FeatureType
