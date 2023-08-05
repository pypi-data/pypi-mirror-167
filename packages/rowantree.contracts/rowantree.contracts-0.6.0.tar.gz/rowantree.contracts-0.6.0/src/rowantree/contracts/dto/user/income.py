""" UserIncome Definition """

from typing import Optional

from pydantic import BaseModel

from ...store_type import StoreType


class UserIncome(BaseModel):
    """
    UserIncome DTO
    Define a user income source.

    Attributes
    ----------
    amount: int
        The amount (number of workers) of the income.
    name: StoreType
        The StoreType of the income.
    description: Optional[str]
        The optional description of the income.
    """

    amount: int
    name: StoreType
    description: Optional[str]
