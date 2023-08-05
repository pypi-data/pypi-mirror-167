""" User Feature State Definition """

from typing import Optional

from pydantic import BaseModel

from ...feature_details import FeatureDetails


class UserFeatureState(BaseModel):
    """
    UserFeatureState DTO

    Attributes
    ----------
    """

    details: FeatureDetails
    description: Optional[str]
