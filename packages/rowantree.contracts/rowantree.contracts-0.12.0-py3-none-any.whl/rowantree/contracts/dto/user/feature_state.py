""" User Feature State Definition """

from typing import Optional

from ...feature_details import FeatureDetails
from ..base_model import BaseModel


class UserFeatureState(BaseModel):
    """
    UserFeatureState DTO

    Attributes
    ----------
    """

    details: FeatureDetails
    description: Optional[str]
