""" UserPopulation Definition """

from pydantic import BaseModel


class UserPopulation(BaseModel):
    """
    UserPopulation DTO
    Defines a user population.

    Attributes
    ----------
    population: int
        The current size of the user population.
    """

    population: int
