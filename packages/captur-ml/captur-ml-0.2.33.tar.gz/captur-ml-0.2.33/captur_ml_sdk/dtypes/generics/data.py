import pydantic

from image import Image
from label import ClassLabel
from prediction import ClassificationPredictionSet

from typing import List


class MongoDBTrainingData(pydantic.BaseModel):
    pass

class MongoDBPredictionData(pydantic.BaseModel):
    pass

class MongoDBEvaluationData(pydantic.BaseModel):
    pass


class TrainingData(pydantic.BaseModel):
    images: List[Image] = pydantic.Field(
        ...,
        description='The list of images used for training'
    )
    labels: List[ClassLabel] = pydantic.Field(
        ...,
        description='The list of class labels used for training'
    )


class PredictionData(pydantic.BaseModel):
    images: List[Image] = pydantic.Field(
        ...,
        description='The list of images used for prediction'
    )


class EvaluationData(pydantic.BaseModel):
    images: List[Image] = pydantic.Field(
        ...,
        description='The list of images used for evaluation'
    )
    labels: List[ClassLabel] = pydantic.Field(
        ...,
        description='The list of class labels used for evaluation'
    )
    predictions: List[ClassificationPredictionSet] = pydantic.Field(
        ...,
        description='The list of predictions used for evaluation'
    )
