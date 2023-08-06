""" Active Feature Response Definition """

from rowantree.contracts import BaseModel, UserFeatureState


class ActiveFeatureResponse(BaseModel):
    """
    Active Feature Response DTO

    Attributes
    ----------
    feature_state: UserFeatureState
        The current active feature details of the user.
    """

    feature_state: UserFeatureState
