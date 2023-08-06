"""" WorldStatus Definition """
from rowantree.common.sdk import BaseModel


class WorldStatus(BaseModel):
    """
    WorldStatus DTO
    Defines the status of the game world.

    Attributes
    ----------
    active_users: set[str]
        A set of active users.
    """

    active_users: set[str]
