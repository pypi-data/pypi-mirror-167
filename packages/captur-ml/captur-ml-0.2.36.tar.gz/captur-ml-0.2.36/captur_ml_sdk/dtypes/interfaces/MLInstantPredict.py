import pydantic

from captur_ml_sdk.dtypes.generics import Endpoint
from captur_ml_sdk.dtypes.results import ImageClassificationResult
from typing import List


class InstantPredictionRequest(pydantic.BaseModel):
    endpoint: Endpoint = pydantic.Field(
        ...,
        description="The ID and location of the VertexAI endpoint to use for prediction.",
    )
    image_url: pydantic.AnyUrl = pydantic.Field(
        ...,
        description="The URL of the image to use for prediction.",
    )
    request_id: str = pydantic.Field(
        "",
        description="Unique ID for the request."
    )


class InstantPredictionResponse(pydantic.BaseModel):
    endpoint: Endpoint = pydantic.Field(
        ...,
        description="The ID and location of the VertexAI endpoint to use for prediction.",
    )
    images: List[ImageClassificationResult] = pydantic.Field(
        ...,
        description='The list of classification results of the images used for the prediction.'
    )
    request_id: str = pydantic.Field(
        ...,
        description="Unique ID for the request."
    )
