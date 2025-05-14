# Test Suite for xSAR Scoring Pipeline

This directory contains a minimal suite of tests designed to verify the reproducibility and consistency of the core scoring functionality implemented in the xSAR pipeline.

> **Note**: These tests do not (yet) constitute full pipeline validation or integration testing. Their current goal is to ensure that key scoring behaviors remain stable across code changes and library upgrades, particularly related to RDKit versioning.

## Purpose

The tests serve the following primary objectives:

- **Check scoring accuracy** against previously validated PBS/NBS outputs.
- **Verify repeatability** of outputs when toggling between precomputed and on-the-fly fingerprinting.
- **Evaluate consistency** across independent datasets (e.g. retrospective test compounds).
- **Detect silent regressions** caused by environment differences (e.g. RDKit updates).

## Tests Overview

| Test File                                                                 | Description                                                                 |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `test_scores_consistency.py`                                             | Compares current PBS/NBS scores to reference for the original dataset.     |
| `test_scores_precomputed_vs_non_precomputed.py`                         | Verifies that internal and external bit generation yield identical results.|
| `test_scores_independent_compounds_vs_precomputed.py`                   | Validates scoring of independent compounds against precomputed references. |

## Data

Reference datasets are located in the `tests/data/` folder and include:

- `Lateral_OriginalRefined-957_BeforeReevaluation_PBS_NBS_rdk_v2022.csv`
- `Retrospective-97_test_PBS_NBS_rdk_v2022.csv`

These PBS and NBS scores were **independently generated using RDKit `v2022.03.3`** with the following fingerprinting configuration:

- `radius=6`
- `nBits=2048`
- `useFeatures=True`

Function call used for ECFP generation of reference data:

```python
AllChem.GetMorganFingerprintAsBitVect(
    mol, radius=6, nBits=2048,
    bitInfo=bi, useFeatures=True
)
```

## Usage

These tests can be run with any compatible Python testing framework such as `unittest` or `pytest`. Example:

```bash
#launched from the xSAR/xsar_model/scripts/tests directory
python -m unittest discover ./
```