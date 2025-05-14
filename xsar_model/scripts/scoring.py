"""
scoring.py

Provides scoring functions for evaluating compound binding likelihood using
bit conservation-based metrics: PBS (Positive Binding Score) and NBS (Negative Binding Score).

These scores are computed using fingerprint bit vectors derived from ECFP (e.g., via `process_dataframe_bits`)
and conserved bit sets identified in a reference dataset.

Dependencies:
    - Pandas
    - NumPy
"""

import numpy as np
import pandas as pd
from typing import Union


def get_bit_conservation_scores_from_binders(df_bits: pd.DataFrame) -> np.ndarray:
    """
    Calculate bit conservation scores from experimentally confirmed binders.

    Args:
        df_bits (pd.DataFrame): Bit-annotated dataframe from `process_dataframe_bits`.
                                Must include MultiIndex column: ('Reference', 'Binding') and 'Connectivity'.

    Returns:
        np.ndarray: Conservation score for each bit (fraction of binders in which bit appears).
    """
    connectivity = df_bits['Fingerprint']
    binding_col = df_bits['Reference']['Binding'].astype(bool)
    binders_idx = binding_col == True
    binders_bits = connectivity[binders_idx]
    scores = binders_bits.sum(axis=0) / max(1, binders_bits.shape[0])
    return scores.values


def get_postive_binding_scores(
    df_bits: pd.DataFrame,
    conserved_binding_bits: Union[np.ndarray, list]
) -> np.ndarray:
    """
    Compute the PBS score (fraction of conserved binding bits present in each compound).

    Args:
        df_bits (pd.DataFrame): Bit-annotated dataframe with 'Fingerprint' columns.
        conserved_binding_bits (array-like): Indices of conserved binding bits.

    Returns:
        np.ndarray: PBS score for each compound (float between 0 and 1).
    """
    if len(conserved_binding_bits) == 0:
        return np.zeros(df_bits.shape[0])
    subset = df_bits['Fingerprint'].iloc[:, conserved_binding_bits]
    return (subset.sum(axis=1) / len(conserved_binding_bits)).values


def get_negative_binding_scores(
    df_bits: pd.DataFrame,
    conserved_non_binding_bits: Union[np.ndarray, list]
) -> np.ndarray:
    """
    Compute the NBS score (1 - fraction of conserved non-binding bits present).

    Args:
        df_bits (pd.DataFrame): Bit-annotated dataframe with 'Fingerprint' columns.
        conserved_non_binding_bits (array-like): Indices of conserved non-binding bits.

    Returns:
        np.ndarray: NBS score for each compound (float between 0 and 1).
    """
    if len(conserved_non_binding_bits) == 0:
        return np.ones(df_bits.shape[0])
    subset = df_bits['Fingerprint'].iloc[:, conserved_non_binding_bits]
    return (1 - subset.sum(axis=1) / len(conserved_non_binding_bits)).values


def predict_PBS_binders(
    df_bits: pd.DataFrame,
    conserved_binding_bits: Union[np.ndarray, list],
) -> np.ndarray:
    """
    Predicts binders based on PBS score exceeding the given threshold.

    Args:
        df_bits (pd.DataFrame): Bit-annotated dataframe with 'Fingerprint'.
        conserved_binding_bits (array-like): Indices of conserved binding bits.

    Returns:
        np.ndarray: Index array of compounds predicted as likely binders.
    """
    scores = get_postive_binding_scores(df_bits, conserved_binding_bits)
    return df_bits.index[scores >= 1.0].values


def predict_NBS_nonbinders(
    df_bits: pd.DataFrame,
    conserved_non_binding_bits: Union[np.ndarray, list],
) -> np.ndarray:
    """
    Predicts non-binders based on NBS score exceeding the given threshold.

    Args:
        df_bits (pd.DataFrame): Bit-annotated dataframe with 'Fingerprint'.
        conserved_non_binding_bits (array-like): Indices of conserved non-binding bits.
        NBS_threshold (float): Minimum NBS score to be considered an unlikely binder.

    Returns:
        np.ndarray: Index array of compounds predicted as unlikely binders.
    """
    scores = get_negative_binding_scores(df_bits, conserved_non_binding_bits)
    return df_bits.index[scores >= 1.0].values
