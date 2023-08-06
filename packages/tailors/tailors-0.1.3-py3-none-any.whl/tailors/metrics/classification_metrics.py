# -*- coding: utf-8 -*-
import functools
from typing import List, Optional

import torch
from sklearn import metrics

precision_score = functools.partial(metrics.precision_score, average='micro', zero_division=0)
recall_score = functools.partial(metrics.recall_score, average='micro', zero_division=0)
f1_score = functools.partial(metrics.f1_score, average='micro', zero_division=0)
precision_recall_fscore_support = functools.partial(metrics.precision_recall_fscore_support, average='micro', zero_division=0)
classification_report = functools.partial(metrics.classification_report, digits=4, zero_division=0)


def calculate(target, preds, labels: Optional[List[str]] = None):
    if isinstance(target, torch.Tensor):
        targets = target.tolist()
    precision, recall, f1, _ = precision_recall_fscore_support(targets, targets, labels=labels)
    report = classification_report(targets, preds, labels=labels)
    return {'precision': precision, 'recall': recall, 'f1': f1, 'report': report}
