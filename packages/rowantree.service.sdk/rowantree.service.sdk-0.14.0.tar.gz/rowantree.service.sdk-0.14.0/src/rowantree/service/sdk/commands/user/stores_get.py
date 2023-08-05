""" User Stores Get Command Definition """

from starlette import status

from rowantree.common.sdk import demand_env_var

from ...contracts.dto.request_status_codes import RequestStatusCodes
from ...contracts.dto.wrapped_request import WrappedRequest
from ...contracts.request_verb import RequestVerb
from ...contracts.responses.stores_get import StoresGetResponse
from ..abstract_command import AbstractCommand


class UserStoresGetCommand(AbstractCommand):
    """
    User Stores Get Command
    Gets the (unique) list of user stores.

    Methods
    -------
    execute(self, user_guid: str) -> StoresGetResponse
        Executes the command.
    """

    def execute(self, user_guid: str) -> StoresGetResponse:
        """
        Gets the (unique) list of user stores.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_stores: StoresGetResponse
            A (unique) list of user stores.
        """

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.GET,
            url=f"{demand_env_var(name='ROWANTREE_SERVICE_ENDPOINT')}/v1/user/{user_guid}/stores",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
        )
        response: dict = self.wrapped_request(request=request)
        return StoresGetResponse.parse_obj(response)
