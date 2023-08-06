# -*- coding: utf-8 -*-
from typing import Optional

import numpy as np


def divide(numerator, denominator):
    """Performs division and handles divide-by-zero. """
    mask = denominator == 0.0
    denominator = denominator.copy()
    denominator[mask] = 1  # avoid infs/nans
    result = numerator / denominator

    if not np.any(mask):
        return result

    result[mask] = 0.0
    return result


def f_score(precision, recall, beta=1.0):
    beta2 = beta ** 2
    if np.isposinf(beta):
        return recall
    else:
        denom = beta2 * precision + recall

        denom[denom == 0.] = 1  # avoid division by 0
        return (1 + beta2) * precision * recall / denom


def precision_recall_f1_support(pred_sum, tp_sum, true_sum, average: Optional[str] = None):
    weights = None
    if average == 'micro':
        tp_sum = np.array([tp_sum.sum()])
        pred_sum = np.array([pred_sum.sum()])
        true_sum = np.array([true_sum.sum()])
    elif average == 'weighted':
        weights = true_sum

    precision = divide(tp_sum, pred_sum)
    recall = divide(tp_sum, true_sum)
    f1 = f_score(precision, recall)

    if average is not None:
        precision = np.average(precision, weights=weights)
        recall = np.average(recall, weights=weights)
        f1 = np.average(f1, weights=weights)
        true_sum = sum(true_sum)
    return precision, recall, f1, true_sum
