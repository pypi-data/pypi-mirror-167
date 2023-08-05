import numpy as np


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def softmax(x: np.ndarray, axis: int) -> np.ndarray:
    x_max = np.amax(x, axis=axis, keepdims=True)
    exp_x_shifted = np.exp(x - x_max)
    return exp_x_shifted / np.sum(exp_x_shifted, axis=axis, keepdims=True)


def cross_entropy_on_logits(logits, labels, axis):
    logits = logits - logits.max(axis=axis, keepdims=True)
    e = np.exp(logits)
    s = np.sum(e, axis=axis)
    labels_expanded = np.expand_dims(labels, axis=axis)
    taken = np.take_along_axis(logits, labels_expanded, axis=axis)
    ces = np.log(s) - taken.squeeze(axis=axis)
    return ces


def cross_entropy_on_proba(proba, labels, axis):
    labels_expanded = np.expand_dims(labels, axis=axis)
    taken = np.take_along_axis(proba, labels_expanded, axis=axis)
    ces = -np.log(taken).squeeze(axis)
    return ces


def binary_cross_entropy_on_proba(proba, labels, eps=1e-7):
    # Based on https://stackoverflow.com/a/67616451
    y_pred = np.clip(proba, eps, 1 - eps)
    term_0 = (1 - labels) * np.log(1 - y_pred + eps)
    term_1 = labels * np.log(y_pred + eps)
    return -(term_0 + term_1)


def binary_cross_entropy_on_logits(logits, labels):
    return binary_cross_entropy_on_proba(sigmoid(logits), labels)


def absolute_error(y_pred, y_true):
    return np.abs(y_pred - y_true)


def squared_error(y_pred, y_true):
    diff = y_pred - y_true
    return diff * diff
