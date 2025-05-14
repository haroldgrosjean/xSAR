"""
bit_processing.py

This module provides utility functions for identifying and classifying fingerprint bits
based on their occurrence patterns in molecular datasets. These classifications include
unsampled, conserved binding, conserved non-binding, and unconserved bits.

Requires:
    - Pandas
    - NumPy
"""

import numpy as np
import pandas as pd
from typing import Union


def get_unsampled_bits(df_bits: pd.DataFrame) -> np.ndarray:
    """
    Identify fingerprint bits that are never present in the dataset.

    Args:
        df_bits (pd.DataFrame): DataFrame with MultiIndex columns ('Fingerprint', Bit).

    Returns:
        np.ndarray: Array of unsampled bit indices (ints).
    """
    bit_sums = df_bits['Fingerprint'].sum(axis=0)
    unsampled = bit_sums[bit_sums == 0].index
    return np.array([bit_name for bit_name in unsampled])


def get_conserved_binding_bits(
    conservation_scores: Union[np.ndarray, pd.Series],
) -> np.ndarray:
    """
    Identify bits that are consistently present in binders.

    Args:
        conservation_scores (np.ndarray or pd.Series): Bit conservation scores (0–1).

    Returns:
        np.ndarray: Indices of conserved binding bits.
    """
    return np.argwhere(conservation_scores >= 1.0).flatten()


def get_conserved_non_binding_bits(
    conservation_scores: Union[np.ndarray, pd.Series],
    unsampled_bits: np.ndarray,
) -> np.ndarray:
    """
    Identify bits that are absent or very rarely present in binders
    and are not entirely unsampled.

    Args:
        conservation_scores (np.ndarray or pd.Series): Bit conservation scores (0–1).
        unsampled_bits (np.ndarray): Bit indices that were never sampled.

    Returns:
        np.ndarray: Indices of conserved non-binding bits.
    """
    non_binding = np.argwhere(conservation_scores <= 0.0).flatten()
    return np.setdiff1d(non_binding, unsampled_bits)


def get_unconservative_bits(
    conservation_scores: Union[np.ndarray, pd.Series],
) -> np.ndarray:
    """
    Identify bits that are inconsistently present across binders
    (i.e., not strongly conserved nor strongly excluded).

    Args:
        conservation_scores (np.ndarray or pd.Series): Bit conservation scores (0–1).

    Returns:
        np.ndarray: Indices of bits with ambiguous conservation behavior.
    """
    below_binding = np.argwhere(conservation_scores < 1.0).flatten()
    above_nonbinding = np.argwhere(conservation_scores > 0.0).flatten()
    return np.intersect1d(below_binding, above_nonbinding)
