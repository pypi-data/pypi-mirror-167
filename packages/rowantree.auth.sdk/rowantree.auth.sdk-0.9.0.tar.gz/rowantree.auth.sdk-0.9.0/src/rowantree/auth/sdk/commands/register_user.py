""" Register User Command Definition """

from starlette import status

from rowantree.common.sdk import demand_env_var

from ..contracts.dto.request_status_codes import RequestStatusCodes
from ..contracts.dto.token import Token
from ..contracts.dto.wrapped_request import WrappedRequest
from ..contracts.request_verb import RequestVerb
from ..contracts.requests.register_user_request import RegisterUserRequest
from .abstract_command import AbstractCommand


class RegisterUserCommand(AbstractCommand):
    """
    Register User Command

    Methods
    -------
    execute(self, request: User) -> None
        Register User
    """

    def execute(self, request: RegisterUserRequest) -> Token:
        """
        Register User

        Parameters
        ----------
        request: RegisterUserRequest
        """

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.POST,
            url=f"{demand_env_var(name='ACCESS_AUTH_ENDPOINT')}/v1/auth/register",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[], retry=[]),
            data=request.dict(),
        )
        response: dict = self.wrapped_request(request=request)
        return Token.parse_obj(response)
