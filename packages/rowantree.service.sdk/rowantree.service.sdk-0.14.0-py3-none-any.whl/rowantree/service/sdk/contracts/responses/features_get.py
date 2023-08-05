""" FeaturesGetResponse Definition """
from pydantic import BaseModel

from rowantree.contracts import FeatureType


class FeaturesGetResponse(BaseModel):
    """
    FeaturesGetResponse DTO
    Defines a list of known user features (locations) of the game world.

    Attributes
    ----------
    features: set[FeatureType]
        A set of user feature types.
    """

    features: set[FeatureType]
