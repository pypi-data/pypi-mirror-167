import pydantic

from captur_ml_sdk.dtypes.generics import ClassLabel, AuditLabel, ClassificationPredictionSet
from captur_ml_sdk.dtypes.generics.metrics import ClassificationStandardMetrics, ClassificationAuditMetrics
from typing import Dict, List, Optional


class ModelEvaluationRequest(pydantic.BaseModel):
    labels: List[ClassLabel] = pydantic.Field(
        ...,
        description="List of best class labels for each image.",
    )
    audit_labels: Optional[List[AuditLabel]] = pydantic.Field(
        None,
        description="List of acceptable (audit) labels for each image"
    )
    predictions: List[ClassificationPredictionSet] = pydantic.Field(
        ...,
        description="List of sets of model predictions for each image.",
    )
    mapping: Optional[Dict[str, str]] = pydantic.Field(
        None,
        description="Class to decision mapping dictionary.",
    )
    metrics: Optional[List[str]] = pydantic.Field(
        ...,
        description="List of metrics to evaluate.",
    )
    is_external: Optional[bool] = pydantic.Field(
        True,
        description="Whether request is coming from outside of ML team. Metrics are limited if so.",
    )
    request_id: str = pydantic.Field(
        "",
        description="Unique ID for the request."
    )
    webhooks: List[pydantic.AnyUrl] = pydantic.Field(
        ...,
        description="List of webhooks to which the prediction results will be sent.",
    )

class ModelEvaluationResponse(pydantic.BaseModel):
    standard_classification_metrics: Optional[ClassificationStandardMetrics] = pydantic.Field(
        "",
        description="Set of metrics calculated at the class level using the standard method.",
    )
    audit_classification_metrics: Optional[ClassificationAuditMetrics] = pydantic.Field(
        ...,
        description='Set of metrics calculated at the class level using the audit method.'
    )
    standard_mapped_classification_metrics: Optional[ClassificationStandardMetrics] = pydantic.Field(
        "",
        description="Set of metrics calculated at the decision level using the standard method.",
    )
    audit_mapped_classification_metrics: Optional[ClassificationAuditMetrics] = pydantic.Field(
        ...,
        description='Set of metrics calculated at the decision level using the audit method.'
    )
    request_id: str = pydantic.Field(
        "",
        description="Unique ID for the request."
    )
