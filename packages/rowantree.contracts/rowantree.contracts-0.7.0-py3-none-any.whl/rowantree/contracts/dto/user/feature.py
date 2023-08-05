""" User Feature Definition """

from typing import Optional

from pydantic import BaseModel

from ...feature_type import FeatureType


class UserFeature(BaseModel):
    """
    UserFeature DTO
    Defines a user feature (world locations).

    Attributes
    ----------
    name: FeatureType
        The FeatureType of the feature.
    description: Optional[str]
        The description of the feature.
    """

    name: FeatureType
    description: Optional[str]
