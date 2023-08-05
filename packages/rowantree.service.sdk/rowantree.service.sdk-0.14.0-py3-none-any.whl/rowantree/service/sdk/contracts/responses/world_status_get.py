"""" WorldStatusGetResponse Definition """
from pydantic import BaseModel


class WorldStatusGetResponse(BaseModel):
    """
    WorldStatusGetResponse DTO
    Defines the status of the game world.

    Attributes
    ----------
    active_users: set[str]
        A set of active users.
    """

    active_users: set[str]
