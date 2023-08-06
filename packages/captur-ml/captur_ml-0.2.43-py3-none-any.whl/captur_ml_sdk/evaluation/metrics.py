import abc
import math
import torch
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from torchmetrics import (
    Accuracy,
    F1Score,
    Precision,
    Recall,
    ConfusionMatrix,
)

from typing import Dict, List, Union


class Metrics(metaclass=abc.ABCMeta):
    def __init__(self, labels, predictions, metrics: List[str] = None, is_external: bool = False) -> None:
        super().__init__()
        self.labels = labels
        self.predictions = predictions
        self.metrics = metrics
        self.is_external = is_external

    @abc.abstractmethod
    def external_metrics(self) -> Dict:
        pass

    @abc.abstractmethod
    def internal_metrics(self) -> Dict:
        pass

    def calculate(self) -> Dict:
        metric_group = self.external_metrics()
        if not self.is_external:
            metric_group = self.internal_metrics()

        metric_list = metric_group.keys()
        if self.metrics is not None and not self.is_external:
            metric_list = self.metrics

        metrics_dict = {}
        for metric in metric_list:
            metrics_dict[metric] = metric_group[metric]()
        return metrics_dict

    @staticmethod
    def dictify_per_class_metrics(classes, result) -> Dict[str, Union[float, None]]:
        return {
            class_name: score for class_name, score in zip(classes, result)
        }

    @staticmethod
    def csvify_confusion_matrix(classes: List[str], confusion_matrix: List[List[int]]) -> List[str]:
        csv = []
        num_classes = len(classes)
        for i in range(num_classes):
            csv_string = str(classes[i]) + ","
            for j in range(num_classes):
                csv_string += str(confusion_matrix[i][j])
                if j < num_classes - 1:
                    csv_string += ","
            csv.append(csv_string)
        return csv

    @staticmethod
    def noneify_nans(result_list: List) -> List:
        for i in range(len(result_list)):
            if math.isnan(result_list[i]):
                result_list[i] = None
        return result_list


class ClassificationMetrics(Metrics):
    def __init__(self, predictions: torch.Tensor, labels: torch.Tensor, classes: List[str], metrics: List[str] = None, top_k: int = None, is_external: bool = True) -> None:
        """Calculates classification metrics from predictions and labels.

        Args:
            predictions (torch.Tensor): Array of model predictions of shape (N, C) where N is
                                        the number of examples and C is the number of classes.
            labels (torch.Tensor): Array of ground truth labels of shape (N), where N is the
                                   number of examples.
            classes (List[str]): Array of class names.
            metrics (List[str], optional): List of metrics to be calculated. Defaults to None.
            top_k (int, optional): Number of the highest probability score predictions considered
                                   for choosing the correct label. Defaults to None.
            is_external (bool, optional): Whether to return only those metrics suitable for external
                                          purposes. Defaults to False.

        Raises:
            TypeError: Raised if the predictions or labels are not torch.Tensor.
            ValueError: Raised if the value for top_k is less than 1.
            ValueError: Raised if the value for top_k is greater or equal to the number of classes in the predictions.
        """
        super().__init__(labels, predictions, metrics, is_external)

        if not isinstance(predictions, torch.Tensor):
            raise TypeError(
                f"Invalid type for predictions {type(predictions)}, must be type torch.Tensor")
        if not isinstance(labels, torch.Tensor):
            raise TypeError(
                f"Invalid type for labels {type(labels)}, must be type torch.Tensor")

        self.classes = classes
        self.num_classes = len(classes)

        if top_k is None:
            top_k = 1
        if top_k <= 0:
            raise ValueError(f"Invalid value for top K {top_k}")
        self.top_k = top_k

        if self.top_k >= self.num_classes:
            raise ValueError(
                f"top_k ({self.top_k}) must be less than number of classes ({self.num_classes})")

        self.is_external = is_external

    def accuracy(self) -> float:
        """Calculates top-k accuracy on the predictions and labels.

        Returns:
            float: Top-k accuracy.
        """
        accuracy_fn = Accuracy(
            num_classes=self.num_classes, top_k=self.top_k)
        return accuracy_fn(self.predictions, self.labels).item()

    def conf_matrix(self) -> List[str]:
        """Calculates confusion matrix for the predictions and labels.

        Returns:
            List: Confusion matrix.
        """
        confusion_matrix_fn = ConfusionMatrix(num_classes=self.num_classes)
        conf_mat = confusion_matrix_fn(self.predictions, self.labels).tolist()
        return self.csvify_confusion_matrix(self.classes, conf_mat)

    def f1_score(self) -> float:
        """Calculates top-k f1 score on the predictions and labels.

        Returns:
            float: Top-k f1 score.
        """
        f1_score_fn = F1Score(num_classes=self.num_classes, top_k=self.top_k)
        return f1_score_fn(self.predictions, self.labels).item()

    def f1_score_per_class(self) -> Dict[str, Union[float, None]]:
        """Calculates top-k f1 score per class on the predictions and labels.

        Returns:
            Dict[str, float]: Dictionary of top-k f1 score per class.
        """
        f1_score_per_class_fn = F1Score(
            num_classes=self.num_classes, average=None)
        result = f1_score_per_class_fn(self.predictions, self.labels).tolist()
        result = self.noneify_nans(result)
        return self.dictify_per_class_metrics(result, self.classes)

    def precision(self) -> float:
        """Calculates top-k precision on the predictions and labels.

        Returns:
            float: Top-k precision.
        """
        self.precision = Precision(
            num_classes=self.num_classes, top_k=self.top_k)
        return self.precision(self.predictions, self.labels).item()

    def precision_per_class(self) -> Dict[str, Union[float, None]]:
        """Calculates top-k precision per class on the predictions and labels.

        Returns:
            Dict[str, float]: Dictionary of top-k precision per class.
        """
        self.precision_per_class = Precision(
            num_classes=self.num_classes, top_k=self.top_k, average=None)
        result = self.precision_per_class(self.predictions, self.labels).tolist()
        result = self.noneify_nans(result)
        return self.dictify_per_class_metrics(self.classes, result)

    def recall(self) -> float:
        """Calculates top-k recall on the predictions and labels.

        Returns:
            float: Top-k recall.
        """
        self.recall = Recall(num_classes=self.num_classes, top_k=self.top_k)
        return self.recall(self.predictions, self.labels).item()

    def recall_per_class(self) -> Dict[str, Union[float, None]]:
        """Calculates top-k recall per class on the predictions and labels.

        Returns:
            Dict[str, float]: Dictionary of top-k recall per class.
        """
        self.recall_per_class = Recall(
            num_classes=self.num_classes, stop_k=self.top_k, average=None)
        result = self.recall_per_class(self.predictions, self.labels).tolist()
        result = self.noneify_nans(result)
        return self.dictify_per_class_metrics(self.classes, result)

    def external_metrics(self) -> Dict:
        return {
            "accuracy": self.accuracy
        }

    def internal_metrics(self) -> Dict:
        return {
            "accuracy": self.accuracy,
            "f1_score": self.f1_score,
            "f1_score_per_class": self.f1_score_per_class,
            "precision": self.precision,
            "precision_per_class": self.precision_per_class,
            "recall": self.recall,
            "recall_per_class": self.recall_per_class,
            "confusion_matrix": self.conf_matrix
        }


class AuditMetrics(Metrics):
    def __init__(self, audit_labels: List[List[str]], predictions: List[str], is_external: bool = True) -> None:
        super().__init__(labels=audit_labels, predictions=predictions, is_external=is_external)

    def audit_accuracy(self) -> float:
        count_correct = 0
        for al, p in zip(self.labels, self.predictions):
            count_correct += p in al
        return count_correct / len(self.predictions)

    def audit_precision_per_class(self) -> Dict[str, Union[float, None]]:
        all_predicted_classes = list(set(self.predictions))
        all_label_classes = list(set([num for sublist in self.labels for num in sublist]))
        precision_dict = {}
        for cls in all_predicted_classes:
            audit = 0
            count = 0
            for i in range(len(self.predictions)):
                if self.predictions[i] == cls:
                    count += 1
                    if self.predictions[i] in self.labels[i]:
                        audit += 1
            precision = audit / count
            precision_dict[cls] = precision
        for lbl in all_label_classes:
            if lbl not in precision_dict:
                precision_dict[lbl] = None
        return precision_dict

    def external_metrics(self) -> Dict:
        return {
            "accuracy": self.audit_accuracy
        }

    def internal_metrics(self) -> Dict:
        return {
            "accuracy": self.audit_accuracy,
            "precision_per_class": self.audit_precision_per_class,
        }


class MappedClassificationMetrics(Metrics):
    def __init__(self, labels: List[str], predictions: List[str], classes: List[str], metrics: List[str] = None, is_external: bool = True) -> None:
        super().__init__(labels, predictions, metrics, is_external)
        self.classes = classes

    def accuracy(self) -> float:
        return accuracy_score(
            self.labels,
            self.predictions,
        )

    def confusion_matrix(self) -> List[str]:
        conf_mat = confusion_matrix(
            self.labels,
            self.predictions,
            labels=self.classes
        ).tolist()
        return self.csvify_confusion_matrix(self.classes, conf_mat)

    def f1_score(self) -> float:
        return f1_score(
            self.labels,
            self.predictions,
            average="micro",
            labels=self.classes,
            zero_division=0
        )

    def f1_score_per_class(self) -> Dict[str, Union[float, None]]:
        result = f1_score(
            self.labels,
            self.predictions,
            average=None,
            labels=self.classes,
            zero_division=0
        )
        return self.dictify_per_class_metrics(self.classes, result)

    def precision(self) -> float:
        return precision_score(
            self.labels,
            self.predictions,
            average="micro",
            labels=self.classes,
            zero_division=0
        )

    def precision_per_class(self) -> Dict[str, Union[float, None]]:
        result = precision_score(
            self.labels,
            self.predictions,
            average=None,
            labels=self.classes,
            zero_division=0
        )
        return self.dictify_per_class_metrics(self.classes, result)

    def recall(self) -> float:
        return recall_score(
            self.labels,
            self.predictions,
            average="micro",
            labels=self.classes,
            zero_division=0
        )

    def recall_per_class(self) -> Dict[str, Union[float, None]]:
        result = recall_score(
            self.labels,
            self.predictions,
            average=None,
            labels=self.classes,
            zero_division=0
        )
        return self.dictify_per_class_metrics(self.classes, result)

    def external_metrics(self) -> Dict:
        return {
            "accuracy": self.accuracy
        }

    def internal_metrics(self) -> Dict:
        return {
            "accuracy": self.accuracy,
            "f1_score": self.f1_score,
            "f1_score_per_class": self.f1_score_per_class,
            "precision": self.precision,
            "precision_per_class": self.precision_per_class,
            "recall": self.recall,
            "recall_per_class": self.recall_per_class,
            "confusion_matrix": self.confusion_matrix
        }


class DetectionMetrics(Metrics):
    pass


class SemSegMetrics(Metrics):
    pass
