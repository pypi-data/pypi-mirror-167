""" UserIncome Definition """

from typing import Optional

from ...store_type import StoreType
from ..base_model import BaseModel


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
