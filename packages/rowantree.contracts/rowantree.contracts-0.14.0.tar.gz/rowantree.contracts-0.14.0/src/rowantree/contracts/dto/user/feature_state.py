""" User Feature State Definition """

from typing import Optional

from ...feature_details import FeatureDetails
from ...feature_type import FeatureType
from ..base_model import BaseModel


class UserFeatureState(BaseModel):
    """
    UserFeatureState DTO

    Attributes
    ----------
    """

    name: Optional[FeatureType]
    details: Optional[FeatureDetails]
    description: Optional[str]
