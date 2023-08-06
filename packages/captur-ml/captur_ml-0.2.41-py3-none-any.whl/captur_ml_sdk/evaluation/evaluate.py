from captur_ml_sdk.evaluation.dataset import ClassificationDataset, MappedClassificationDataset
from captur_ml_sdk.evaluation.metrics import AuditMetrics, ClassificationMetrics, MappedClassificationMetrics

from typing import Dict, List, Union


def evaluate_classification_dataset_standard(
    dataset: ClassificationDataset,
    metric_list: List[str] = None,
    is_external: bool = False,
    top_k: int = None
) -> Dict[str, float]:

    metrics = ClassificationMetrics(
        predictions=dataset.torch_predictions,
        labels=dataset.torch_labels,
        metrics=metric_list, top_k=top_k, is_external=is_external
    ).calculate()
    return metrics


def evaluate_classification_dataset_audit(
    dataset: ClassificationDataset,
    is_external: bool = False,
) -> Union[Dict[str, float], None]:

    metrics = None
    if dataset.audit_labels:
        metrics = AuditMetrics(
            audit_metrics=dataset.audit_labels,
            predictions=dataset.top_predictions,
            is_external=is_external
        ).calculate()
    return metrics


def evaluate_mapped_classification_dataset_standard(
    dataset: ClassificationDataset,
    mapping: Union[Dict[str, str], None] = None,
    metric_list: List[str] = None,
    is_external: bool = False,
) -> Dict[str, float]:

    metrics = None
    if mapping:
        mapped_dataset = MappedClassificationDataset.map_dataset(
            dataset=dataset,
            mapping=mapping,
        )
        metrics = MappedClassificationMetrics(
            labels=mapped_dataset.labels,
            predictions=mapped_dataset.predictions,
            classes=mapped_dataset.classes,
            metrics=metric_list,
            is_external=is_external,
        ).calculate()
    return metrics


def evaluate_mapped_classification_dataset_audit(
    dataset: ClassificationDataset,
    mapping: Union[Dict[str, str], None] = None,
    is_external: bool = False,
) -> Dict[str, float]:

    metrics = None
    if mapping and dataset.audit_labels:
        mapped_dataset = MappedClassificationDataset.map_dataset(
            dataset=dataset,
            mapping=mapping,
        )
        metrics = AuditMetrics(
            audit_labels=mapped_dataset.audit_labels,
            predictions=mapped_dataset.predictions,
            is_external=is_external
        ).calculate()
    return metrics
