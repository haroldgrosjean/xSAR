"""
fingerprints.py

This module handles the generation and formatting of extended-connectivity fingerprints (ECFP)
for molecules represented by SMILES strings. It is used to transform molecules into bit vectors
for downstream analysis in the xSAR framework.

Dependencies:
    - RDKit
    - NumPy
    - Pandas
"""

from typing import Optional
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem, rdFingerprintGenerator
from rdkit.DataStructs import ConvertToNumpyArray

def compute_ecfp_descriptor(
    smiles: str,
    radius: int = 6,
    nBits: int = 2048,
    useFeatures: bool = True
) -> Optional[np.ndarray]:
    """
    Generate a Morgan fingerprint (ECFP) from a SMILES string using the modern RDKit FingerprintGenerator API.

    Args:
        smiles (str): Molecule as a SMILES string.
        radius (int): Radius of fingerprint (default: 6).
        nBits (int): Length of the fingerprint bit vector (default: 2048).
        useFeatures (bool): Whether to use atom feature invariants (default: True).

    Returns:
        Optional[np.ndarray]: The fingerprint as a NumPy array, or None if parsing fails.
    """
    if not smiles:
        return None

    try:
        ps = Chem.SmilesParserParams()
        ps.removeHs = False
        ps.sanitize = True
        mol = Chem.MolFromSmiles(smiles, ps)
    except Exception:
        return None

    if mol is None:
        return None

    # Select atom invariants generator
    atom_inv = (
        rdFingerprintGenerator.GetMorganFeatureAtomInvGen()
        if useFeatures else rdFingerprintGenerator.GetMorganAtomInvGen()
    )

    # Build generator
    factory = rdFingerprintGenerator.GetMorganGenerator(
        radius=radius,
        fpSize=nBits,
        atomInvariantsGenerator=atom_inv,
        includeChirality=False
    )

    # Generate fingerprint as NumPy array
    return factory.GetFingerprintAsNumPy(mol)

def compute_ecfp_descriptor_legacy(
    smiles: str,
    radius: int = 6,
    nBits: int = 2048,
    useFeatures: bool = True
) -> Optional[np.ndarray]:
    """
    Generate a Morgan fingerprint (ECFP) from a SMILES string.

    Args:
        smiles (str): Molecule as a SMILES string.
        radius (int): Radius of fingerprint (default: 6).
        nBits (int): Length of the fingerprint bit vector (default: 2048).
        useFeatures (bool): Whether to use atom features (default: True).

    Returns:
        Optional[np.ndarray]:
            - The fingerprint as a numpy array.

    .. deprecated::
       This function uses RDKit <2025 API and is deprecated.
       This function was employed as the initial xSAR research was being conducted and is therefore showed here
       for transparency.
       Use `compute_ecfp_descriptor` instead.
    """
    if not smiles:
        return None

    try:
        ps = Chem.SmilesParserParams()
        ps.removeHs = False
        ps.sanitize = True
        mol = Chem.MolFromSmiles(smiles, ps)
    except Exception:
        return None

    if mol is None:
        return None

    fp = AllChem.GetMorganFingerprintAsBitVect(
        mol,
        radius=radius,
        nBits=nBits,
        useFeatures=useFeatures,
    )

    arr = np.zeros((nBits,), dtype=np.int8)
    ConvertToNumpyArray(fp, arr)
    return arr


def process_dataframe_bits(
    df: pd.DataFrame,
    radius: int = 6,
    nBits: int = 2048,
    useFeatures: bool = True
) -> pd.DataFrame:
    """
    Process a compound dataframe to compute ECFP fingerprints and format the result
    as a MultiIndexed DataFrame with compound metadata and fingerprint bits.

    Each compound row is indexed as ('Compound', i), and columns are MultiIndexed with
    'Reference' metadata (e.g., Name, Smiles, Binding) and 'Fingerprint' bit values.

    If a "Binding" column is present in the input DataFrame, it will be cast to boolean.
    Otherwise, the result will not include a binding annotation.

    Args:
        df (pd.DataFrame): Input DataFrame with at least "Name" and "Smiles" columns.
                           Optionally includes a "Binding" column (bool or int).
        radius (int, optional): Radius for the ECFP (Morgan) fingerprint. Default is 6.
        nBits (int, optional): Size (bit length) of the fingerprint. Default is 2048.
        useFeatures (bool, optional): Whether to use atom features in fingerprint generation.

    Returns:
        pd.DataFrame: A MultiIndexed DataFrame where rows represent compounds and
                      columns include reference metadata and fingerprint bits.
                      Row index: ('Compound', i)
                      Column index: [('Reference', col), ..., ('Fingerprint', bit), ...]
    """
    ref_cols = ["Name", "Smiles"]
    if "Binding" in df.columns:
        ref_cols.append("Binding")
        df["Binding"] = df["Binding"].astype(bool)

    fingerprint_cols = list(range(nBits))
    bit_rows = []
    valid_rows = []

    for _, row in df.iterrows():
        #NOTE: comment/ uncomment here if you wish to employ the legacy code
        fp = compute_ecfp_descriptor(row["Smiles"], radius=radius, nBits=nBits, useFeatures=useFeatures)
        #fp = compute_ecfp_descriptor_legacy(row["Smiles"], radius=radius, nBits=nBits, useFeatures=useFeatures)
        if fp is None:
            print(f"No fingerprint was computed for {row['Smiles']}")
            continue
        bit_rows.append(fp)
        valid_rows.append(row)

    if not bit_rows:
        raise ValueError("No valid SMILES to compute fingerprints.")

    n_skipped = len(df) - len(valid_rows)
    if n_skipped > 0:
        print(f"Skipped {n_skipped} compounds due to invalid SMILES or fingerprint failure.")

    df_ref = pd.DataFrame(valid_rows)[ref_cols].reset_index(drop=True)
    df_bits = pd.DataFrame(bit_rows, columns=fingerprint_cols)

    combined_df = pd.concat([df_ref, df_bits], axis=1)

    # Set MultiIndex columns
    ref_level = [("Reference", col) for col in ref_cols]
    bit_level = [("Fingerprint", i) for i in fingerprint_cols]
    combined_df.columns = pd.MultiIndex.from_tuples(ref_level + bit_level)

    # Set MultiIndex index — all compound rows will now be ('Compound', i)
    compound_idx = [("Compound", i) for i in range(len(combined_df))]
    combined_df.index = pd.MultiIndex.from_tuples(compound_idx)

    return combined_df

