# 📁 data/

This directory contains all datasets used throughout the development, benchmarking, and prospective application of the xSAR (crystallographic Structure–Activity Relationship) model. Each subdirectory corresponds to a key stage of the xSAR workflow, from raw experimental screening through to model evaluation and experimental validation.

---

## 📦 Directory Overview

| Subdirectory | Description |
|--------------|-------------|
| `1_OriginalRefined-957_BeforeReevaluation/` | Initial dataset of 957 fragment elaboration compounds tested via high-throughput X-ray crystallography in crude reaction mixtures. Labels represent uncorrected crystallographic binding outcomes. |
| `2_Retrospective-97/` | Manually curated subset of 97 compounds from the original 957, re-synthesised and re-evaluated to correct false negatives. Used as a ground-truth test set. |
| `3_OriginalRefined-957_AfterReevaluation/` | Full dataset of 957 compounds with corrected binding labels for the Retrospective-97 subset incorporated. Used for final model training and analysis. |
| `4_MethodsBenchmarking/` | Data splits, predictions, and optimised parameters for benchmarking xSAR metrics (PBS, NBS) against traditional ligand-based methods (e.g., Random Forest, Tanimoto similarity). |
| `5_virtual_screening/` | Outputs from a prospective virtual screening campaign using the xSAR model to filter the Enamine REAL database and prioritise 93 candidate compounds (Prospective-93). |
| `6_experimental_validation/` | Kinetic data from grating-coupled interferometry (GCI) assays for the 93 prospectively selected compounds (Prospective-93). Includes raw binding parameters and curated hit selections.

---

## 📌 Usage Notes

- Pose-specific datasets (`lateral`, `diving`, `all`) are provided where applicable to support structure-guided SAR exploration.
- File-level metadata and column descriptions are provided in the individual `README.md` files within each subdirectory.
- All datasets are version-controlled and aligned with experimental stages described in the manuscript.

For full methodological context, please refer to the main paper and the accompanying documentation throughout the repository.
