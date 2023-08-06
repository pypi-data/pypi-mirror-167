import numpy as np
import torch

from captur_ml_sdk.dtypes.generics import Image, ClassLabel, ClassificationPredictionSet, AuditLabel
from typing import Dict, List


class ClassificationDataset(object):
    def __init__(self, labels: List[ClassLabel], prediction_sets: List[ClassificationPredictionSet], audit_labels: List[AuditLabel] = None):
        """Class for processing classification labels and predictions.

        Args:
            labels (List[ClassLabel]): List of ground truth labels for the images.
            prediction_sets (List[ClassificationPredictionSet]): List of model predictions for the images.

        Raises:
            ValueError: Raised if the prediction or label array is empty.
            ValueError: Raised if the number of predictions does not match the number of labels.
            TypeError: Raised if:
                images is a list of type Image
                labels is not a list of type ClassLabel
                prediction_sets is not a List of type ClassificationPredictionSet
            ValueError: Raised if the number of classes in the labels is greater than the number of classes in the predictions.
        """
        if len(prediction_sets) < 1:
            raise ValueError("Predictions cannot be an empty array")
        if len(labels) < 1:
            raise ValueError("Labels cannot be an empty array")
        if len(labels) != len(prediction_sets):
            raise ValueError(
                f"Number of labels {len(labels)} does not match number of predictions {len(prediction_sets)}")

        if not isinstance(prediction_sets[0], ClassificationPredictionSet):
            raise TypeError(
                f"Prediction sets is type {type(prediction_sets[0])} but must be of type ClassificationPredictionSet (see captur_ml_sdk.dtypes.generics)"
            )
        if not isinstance(labels[0], ClassLabel):
            raise TypeError(
                f"Labels is type {type(labels[0])} but must be of type ClassLabel (see captur_ml_sdk.dtypes.generics)"
            )

        self.labels = [label.className for label in labels]

        if len(np.unique(self.labels)) > len(prediction_sets[0].predictions):
            raise ValueError(
                "Number of classes in labels is greater than the number of classes in predictions")
        self.audit_labels = None
        if audit_labels:
            self.audit_labels = [label.classNames for label in audit_labels]
        self.prediction_sets = prediction_sets
        self.classes = [pred.className for pred in self.prediction_sets[0].predictions]

    @property
    def class_encoding(self):
        return {class_name: i for i, class_name in enumerate(self.classes)}

    @property
    def torch_labels(self):
        encoded_labels = [self.class_encoding(label.className) for label in self.labels]
        return torch.tensor(encoded_labels)

    @property
    def torch_predictions(self):
        ordered_predictions = [
            sorted(prediction_set, key=lambda pred: self.class_encoding[pred["className"]])
            for prediction_set in self.predictions
        ]
        ordered_confidences = [pred.confidence for pred in ordered_predictions]
        return torch.tensor(ordered_confidences)

    @property
    def top_predictions(self):
        return [prediction_set.predictions[0].className for prediction_set in self.prediction_sets]


class MappedClassificationDataset(object):
    def __init__(self, labels: List[str], predictions: List[str], audit_labels: List[List[str]], classes: List[str]):
        self.predictions = predictions
        self.labels = labels
        self.audit_labels = audit_labels
        self.classes = classes

    @classmethod
    def map_dataset(cls, dataset: ClassificationDataset, mapping: Dict[str, str]):
        mapped_preds = [mapping[cls] for cls in dataset.top_predictions]
        mapped_labels = [mapping[cls] for cls in dataset.labels]
        mapped_audit_labels = None
        if dataset.audit_labels:
            mapped_audit_labels = cls.map_nested_array(dataset.audit_labels, mapping)
        mapped_classes = cls.get_unique_mapped_classes(mapping)
        return cls(mapped_preds, mapped_labels, mapped_audit_labels, mapped_classes)

    @staticmethod
    def map_nested_array(nested_array: List[List[str]], mapping: Dict[str, str]):
        mapped_nested_array = []
        for array in nested_array:
            mapped_array = []
            for item in array:
                try:
                    mapped_array.append(mapping[item])
                except KeyError:
                    raise ValueError(f"{item} in audit labels not present in mapping")
            mapped_nested_array.append(mapped_array)
        return mapped_nested_array

    @staticmethod
    def get_unique_mapped_classes(mapping: Dict[str, str]):
        return np.unique(list(mapping.values())).tolist()
