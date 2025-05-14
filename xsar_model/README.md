# xsar_model

This repository holds the core logic and data for xSAR modelling.  
It supports bit-level analysis, compound-level prediction, and chemical space visualization using conservation-derived features from extended-connectivity fingerprints (ECFP).

---

## 📁 Directory Overview

- `scripts/`  
  Contains all functional Python modules used to perform xSAR modelling.
  
- `data/`  
  Placeholder directory to store chemical datasets for scoring and benchmarking.

- `examples/`  
  Contains example notebooks and scripts to demonstrate how to use the xSAR pipeline end-to-end.

---

## 📦 Core Modules

| Script | Purpose |
|--------|---------|
| `fingerprints.py` | Compute and format ECFP bitvectors from SMILES using RDKit. |
| `bit_processing.py` | Identify conserved/non-conserved fingerprint bits based on binding patterns. |
| `scoring.py` | Calculate PBS/NBS scores and predict likely binders or non-binders. |
| `annotation.py` | Annotate compound and bit matrices with interpretive labels and metadata. |
| `pipeline.py` | High-level orchestration: train models, score new molecules, and combine annotations. |
