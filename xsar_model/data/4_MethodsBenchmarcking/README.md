# 📁 4_MethodsBenchmarking

This folder contains benchmarking data for ligand-based classification methods used to distinguish crystallographic binders from non-binders in the `OriginalRefined-957` dataset. These benchmark data serve to evaluate the performance of SAR-derived metrics (PBS and NBS) against standard cheminformatics methods such as random forest classification and Tanimoto similarity scoring.

---

## 📋 Dataset Description

For each pose type (`All`, `Lateral`, `Diving`), compounds were split into:
- **Training set**: 860 compounds from `OriginalRefined-957_BeforeReevaluation`, excluding `Retrospective-97`.
- **Test set**: 97 compounds from `Retrospective-97`, with corrected binding labels from the reevaluation.

Three classification methods were applied:
1. **Random Forest Classifier (RFC)** — trained on the training set and optimised using Optuna against the test ground truth.
2. **Tanimoto similarity (mean and max)** — computed using Morgan fingerprints (radius=6, 2048-bit) with known binders as reference.
3. **PBS and NBS scores** — showed in the examples, and evaluated as described in the manuscript.

Random forest hyperparameters were tuned using Optuna (2,500 trials) and applied using scikit-learn. Model evaluation was based on the **Precision-Recall Area Under Curve (PR-AUC)**, averaged across 200 repeats.
---

## 📄 File contents

Each file is specific to one pose (`All`, `Lateral`, `Diving`) and includes training data, testing data, predictions, and optimised hyperparameters.

| Filename                 | Description 
|--------------------------|-------------
| `All_train.csv`          | Training set (excluding `Retrospective-97`) for all poses.
| `All_test.csv`           | Test set from `Retrospective-97` (corrected labels).
| `All_RFC_HPO.csv`        | Random forest prediction scores (HPO = hyperparameter-optimised).
| `All_best_HP.json`       | Best hyperparameters found via Optuna.
| `Diving_train.csv`       | Training set for diving pose.
| `Diving_test.csv`        | Test set for diving pose.
| `Diving_RFC_HPO.csv`     | Random forest predictions for diving pose.
| `Diving_best_HP.json`    | Best hyperparameters for diving pose.
| `Lateral_train.csv`      | Training set for lateral pose.
| `Lateral_test.csv`       | Test set for lateral pose.
| `Lateral_RFC_HPO.csv`    | Random forest predictions for lateral pose.
| `Lateral_best_HP.json`   | Best hyperparameters for lateral pose.

Each CSV contains:

| Column                         | Description                                
|--------------------------------|--------------------------------------------
| `Name`                         | Internal compound identifier               
| `Smiles`                       | Molecular SMILES representation            
| `Binding`                      | Ground-truth crystallographic outcome: TRUE or FALSE

---

## 🔁 Usage context

These files are used to:
- Random forest hyperparameters optimisation
- **Benchmark ligand-based classifiers** on predicting fragment binding outcomes.
- Compare traditional cheminformatics methods to SAR-derived scores (PBS/NBS).
- Assess the **PR-AUC** performance across methods using statistically grounded metrics.

These benchmarking outputs support the evaluation of the xSAR method's performance in a ligand-only prediction setting.
