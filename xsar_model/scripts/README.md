# xSAR Scripts Directory

This directory contains the core logic and utilities for computing the crystallographic structure–activity relationship (xSAR) scores based on chemical fingerprint conservation analysis. These scripts support the end-to-end xSAR pipeline, including fingerprint generation, bit conservation profiling, scoring, annotation, and batch evaluation.

---

## Module Overview

### `fingerprints.py`

Handles the generation and formatting of extended-connectivity fingerprints (ECFP) using RDKit. This module includes a modern and a legacy interface for creating molecular fingerprints from SMILES strings. It also supports transforming an input dataframe of molecules into a bit matrix suitable for scoring.

---

### `bit_processing.py`

Provides utility functions to classify fingerprint bits based on their conservation in binding compounds. These include detection of unsampled bits, conserved binding bits (CBB), conserved non-binding bits (CNB), and unconserved bits.

---

### `scoring.py`

Implements score computation functions for Positive Binding Score (PBS) and Negative Binding Score (NBS). These scores reflect the presence or absence of conserved fingerprint bits across the dataset and are used to predict compound binding status.

---

### `annotation.py`

Adds metadata annotations to the bit matrix or compound-level tables. Annotations include conservation scores, binding classifications, and boolean predictions based on PBS and NBS. These enriched tables can be used for SAR model interpretation or visualisation.

---

### `pipeline.py`

Provides high-level pipeline functions that orchestrate fingerprint generation, bit conservation analysis, and compound scoring. This includes the main scoring loop for labeled (`analyse_score`) and unlabeled (`score_unmeasured_compounds`) datasets. Also supports precomputed descriptors for integration into broader cheminformatics workflows.

---

### `tests/`

Contains unit tests for validating pipeline outputs and internal consistency, e.g., ensuring identical outputs when scoring precomputed vs. on-the-fly fingerprints.

---

## Typical Workflow

1. Use `process_dataframe_bits` to generate fingerprints.
2. Run `analyse_score` on a labeled dataset to compute conservation statistics and annotate bits.
3. Run `score_unmeasured_compounds` on a test set to predict binding profiles using conservation-derived rules.
4. Use annotations and scores for downstream SAR modeling or compound selection.

---

## Notes

- Fingerprints are stored as MultiIndexed DataFrames with namespaces such as `('Reference', 'Smiles')`, `('Fingerprint', bit)`, and `('Predictions', 'PBS score')`.
- The scoring logic is entirely interpretable and traceable through annotated bits.
- The framework is modular and compatible with both RDKit 2022.x (legacy) and RDKit 2025+ (via `FingerprintGenerator` API).

---

