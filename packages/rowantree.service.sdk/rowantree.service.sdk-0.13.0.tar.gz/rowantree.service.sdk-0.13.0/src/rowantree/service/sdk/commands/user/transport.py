""" User Transport Command Definition """

from starlette import status

from rowantree.common.sdk import demand_env_var

from ...contracts.dto.request_status_codes import RequestStatusCodes
from ...contracts.dto.wrapped_request import WrappedRequest
from ...contracts.request_verb import RequestVerb
from ...contracts.requests.user.transport import UserTransportRequest
from ...contracts.responses.active_feature import ActiveFeatureResponse
from ..abstract_command import AbstractCommand


class UserTransportCommand(AbstractCommand):
    """
    User Transport Command
    Performs a user transport. (feature to feature change)

    Methods
    -------
    execute(self, user_guid: str, request: UserTransportRequest) -> UserFeature
        Executes the command.
    """

    def execute(self, user_guid: str, request: UserTransportRequest) -> ActiveFeatureResponse:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The target user guid.
        request: UserTransportRequest
            The UserTransportRequest to perform.

        Returns
        -------
        user_feature: UserFeature
            The user's new active feature.
        """

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.POST,
            url=f"{demand_env_var(name='ROWANTREE_SERVICE_ENDPOINT')}/v1/user/{user_guid}/transport",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
            data=request.json(by_alias=True),
        )
        response: dict = self.wrapped_request(request=request)
        return ActiveFeatureResponse.parse_obj(response)
