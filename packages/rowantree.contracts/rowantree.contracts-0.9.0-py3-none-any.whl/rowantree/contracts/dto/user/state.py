""" UserState Definition """

from pydantic import BaseModel

from ...feature_details import FeatureDetails
from ...feature_type import FeatureType
from ...store_type import StoreType
from .income import UserIncome
from .notification import UserNotification
from .store import UserStore


class UserState(BaseModel):
    """
    UserState DTO
    Defines a user state.

    Attributes
    ----------
    active: bool
        Whether the user is active server side.
    stores: dict[StoreType, UserStore]
        A dictionary of user stores, keyed by store name.
    incomes: dict[StoreType, UserIncome]
        A dictionary of user incomes, keyed by income name.
    features: set(FeatureType)
        A set of user features.
    active_feature: FeatureType
        The current active user feature (location the user is currently in).
    active_feature_state: FeatureDetails
        The active feature details.
    population: int
        The size of the user population.
    merchants: set[StoreType]
        The (unique) set of user merchants.
    notifications: list[UserNotification]
        A list of most recent server events which occurred to the user.
    """

    active: bool
    stores: dict[StoreType, UserStore]
    incomes: dict[StoreType, UserIncome]
    features: set[FeatureType]
    active_feature: FeatureType
    active_feature_state: FeatureDetails
    population: int
    merchants: set[StoreType]
    notifications: list[UserNotification]
