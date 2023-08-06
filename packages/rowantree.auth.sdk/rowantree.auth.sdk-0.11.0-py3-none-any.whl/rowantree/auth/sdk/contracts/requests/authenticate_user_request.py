""" Authenticate User Request Definition """

from pydantic import BaseModel


class AuthenticateUserRequest(BaseModel):
    """
    Authenticate User Request

    Attributes
    ----------
    username: str
        Username
    password: str
        Plain text password
    """

    username: str
    password: str
