""" FeaturesGetResponse Definition """
from pydantic import BaseModel

from rowantree.contracts import FeatureType, UserFeature


class FeaturesGetResponse(BaseModel):
    """
    FeaturesGetResponse DTO
    Defines a list of known user features (locations) of the game world.

    Attributes
    ----------
    features: dict[FeatureType, UserFeature]
        A dictionary of user features, keyed by feature name.
    """

    features: dict[FeatureType, UserFeature]
