""" User Active Definition """
from pydantic import BaseModel


class UserActive(BaseModel):
    """
    UserActive DTO
    Defines the user active state.

    Attributes
    ----------
    active: bool
        The user active state.
    """

    active: bool
