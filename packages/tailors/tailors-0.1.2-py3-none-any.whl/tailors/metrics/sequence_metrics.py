# -*- coding: utf-8 -*-
import functools

from seqeval import metrics

precision_score = functools.partial(metrics.precision_score, average='micro', zero_division=0)
recall_score = functools.partial(metrics.recall_score, average='micro', zero_division=0)
f1_score = functools.partial(metrics.f1_score, average='micro', zero_division=0)
precision_recall_fscore_support = functools.partial(metrics.sequence_labeling.precision_recall_fscore_support, average='micro', zero_division=0)
classification_report = functools.partial(metrics.classification_report, digits=4, zero_division=0)


def calculate(target_tags, preds_tags):
    precision, recall, f1, _ = precision_recall_fscore_support(target_tags, preds_tags)
    report = classification_report(target_tags, preds_tags)
    return {'precision': precision, 'recall': recall, 'f1': f1, 'report': report}
