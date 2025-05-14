"""
annotation.py

Functions for labeling fingerprint bits and compounds with qualitative information
derived from computed binding scores (PBS, NBS), experimental outcomes, and conservation analysis.

These annotations enrich the bit matrices and compound tables with interpretable metadata
useful for SAR modelling, classification, and visualisation.

Dependencies:
    - NumPy
    - Pandas
"""

import numpy as np
import pandas as pd
from typing import Union


def annotate_bits(
    df_bits: pd.DataFrame,
    conservation_scores: Union[np.ndarray, pd.Series],
    conserved_binding_bits: Union[np.ndarray, list],
    conserved_non_binding_bits: Union[np.ndarray, list],
    unconserved_bits: Union[np.ndarray, list],
    unsampled_bits: Union[np.ndarray, list]
) -> pd.DataFrame:
    """
    Annotate fingerprint bits with conservation scores and labels.

    Returns:
        pd.DataFrame: Annotated dataframe with two extra rows for conservation score and label.
    """
    df_annotated = df_bits.copy()

    # Build new rows: index is first-level 'Bits', second-level each column
    score_row = pd.Series(np.nan, index=df_annotated.columns, name=('Bits', 'Conservation score'))
    label_row = pd.Series('' , index=df_annotated.columns, name=('Bits', 'Conservation label'))

    # Fill conservation scores for Fingerprint columns only
    for i, bit_idx in enumerate(df_annotated['Fingerprint'].columns):
        col = ('Fingerprint', bit_idx)
        score_row[col] = conservation_scores[i]
        if bit_idx in conserved_binding_bits:
            label_row[('Fingerprint', bit_idx)] = 'Binding'
        elif bit_idx in conserved_non_binding_bits:
            label_row[('Fingerprint', bit_idx)] = 'Non-binding'
        elif bit_idx in unconserved_bits:
            label_row[('Fingerprint', bit_idx)] = 'Unconservative'
        elif bit_idx in unsampled_bits:
            label_row[('Fingerprint', bit_idx)] = 'Unsampled'
        else:
            label_row[('Fingerprint', bit_idx)] = 'Unclassified'

    # Only append rows for Fingerprint columns — avoids corrupting dtypes in Reference
    bit_only_cols = df_annotated.columns[df_annotated.columns.get_level_values(0) == 'Fingerprint']
    bit_rows = pd.DataFrame([score_row[bit_only_cols], label_row[bit_only_cols]])
    df_annotated = pd.concat([df_annotated, bit_rows])

    return df_annotated


def annotate_PBS_binders(
    df_bits_annotated: pd.DataFrame,
    positive_binding_scores: np.ndarray,
    indexes_PBS_predicted_binders: Union[np.ndarray, list]
) -> pd.DataFrame:
    """
    Annotate PBS predicted binders.

    Args:
        df_bits_annotated (pd.DataFrame): DataFrame with fingerprint bits and metadata.
        positive_binding_scores (np.ndarray): Array of PBS scores (len = num compounds).
        indexes_PBS_predicted_binders (array): Index values of compounds predicted as predicted binders.

    Returns:
        pd.DataFrame: Annotated dataframe with PBS score and binary predicted binding call.
    """
    df = df_bits_annotated.copy()

    # Identify compound rows using MultiIndex level
    compound_rows = df.index.get_level_values(0) == 'Compound'
    compound_index = df.index[compound_rows]

    # Sanity check
    if len(positive_binding_scores) != len(compound_index):
        raise ValueError(f"Expected {len(compound_index)} PBS scores, got {len(positive_binding_scores)}")

    # Add prediction columns if needed
    if ('Predictions', 'Positive binding score') not in df.columns:
        df[('Predictions', 'Positive binding score')] = np.nan
    if ('Predictions', 'PBS binder') not in df.columns:
        df[('Predictions', 'PBS binder')] = ''

    # Assign values
    df.loc[compound_index, ('Predictions', 'Positive binding score')] = positive_binding_scores
    df.loc[compound_index, ('Predictions', 'PBS binder')] = False

    # Predicted predicted binders
    df.loc[compound_index.intersection(indexes_PBS_predicted_binders), ('Predictions', 'PBS binder')] = True

    return df

def annotate_NBS_nonbinders(
    df_annotated: pd.DataFrame,
    negative_binding_scores: np.ndarray,
    indexes_NBS_predicted_nonbinders: Union[np.ndarray, list]
) -> pd.DataFrame:
    """
    Add NBS score and binary label ("Predicted non-binder") to compound rows.

    Args:
        df_annotated (pd.DataFrame): Bit dataframe after PBS annotation.
        negative_binding_scores (np.ndarray): NBS scores (0–1).
        indexes_NBS_predicted_nonbinders (array): Index values of compounds predicted as Predicted non-binder.

    Returns:
        pd.DataFrame: Further annotated dataframe with NBS score and binary predicted binding call.
    """
    df = df_annotated.copy()

    compound_rows = df.index.get_level_values(0) == 'Compound'
    compound_index = df.index[compound_rows]

    if len(negative_binding_scores) != len(compound_index):
        raise ValueError(f"Expected {len(compound_index)} NBS scores, got {len(negative_binding_scores)}")

    if ('Predictions', 'Negative binding score') not in df.columns:
        df[('Predictions', 'Negative binding score')] = np.nan
    if ('Predictions', 'NBS binder') not in df.columns:
        df[('Predictions', 'NBS binder')] = ''

    df.loc[compound_index, ('Predictions', 'Negative binding score')] = negative_binding_scores
    df.loc[compound_index, ('Predictions', 'NBS binder')] = False

    df.loc[compound_index.intersection(indexes_NBS_predicted_nonbinders), ('Predictions', 'NBS binder')] = True

    return df

