""" UserState Definition """

from pydantic import BaseModel

from ...feature_type import FeatureType
from ...store_type import StoreType
from .feature import UserFeature
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
    features: dict[FeatureType, UserFeature]
        A dictionary of user features, keyed by feature name.
    active_feature: FeatureType
        The current active user feature (location the user is currently in).
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
    features: dict[FeatureType, UserFeature]
    active_feature: FeatureType
    population: int
    merchants: set[StoreType]
    notifications: list[UserNotification]
