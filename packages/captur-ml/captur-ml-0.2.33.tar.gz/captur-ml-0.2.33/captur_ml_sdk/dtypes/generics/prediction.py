import pydantic

from typing import List


class ClassificationPrediction(pydantic.BaseModel):
    id: str = pydantic.Field(
        "",
        description='A unique identifier of the Prediction'
    )
    className: str = pydantic.Field(
        ...,
        description='A human-readable name of the Prediction'
    )
    confidence: float = pydantic.Field(
        ...,
        description='The statistical confidence of the Prediction'
    )


class ClassificationPredictionSet(pydantic.BaseModel):
    predictions: List[ClassificationPrediction] = pydantic.Field(
        ...,
        description='The list of predictions'
    )
