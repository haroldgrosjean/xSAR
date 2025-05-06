# 📁 2_Retrospective-97

This folder contains the **Retrospective-97** dataset: a curated subset of 97 compounds from the OriginalRefined-957 set that were re-purchased in purified form and re-evaluated via high-resolution X-ray crystallography. These data represent the **corrected binding outcomes** for this subset, serving as the experimental ground truth for benchmarking.

---

## 📋 Dataset Description

The 97 compounds included here were selected from the OriginalRefined-957 set based on:
1. **Availability in Enamine** in purified form.
2. **Score-driven sampling** across six model ensembles (PBS and NBS across All, Lateral, and Diving poses).
3. **Budget-aware diversity selection**, designed to cover a wide range of score values.

This process yielded 150 candidate compounds across ensembles, with 97 non-overlapping compounds ultimately purchased and tested. Each of the 97 compounds was scored under all six ensemble schemes.

Each compound was labeled with a binary outcome based on manual crystallographic reevaluation:
- **TRUE** = "binder", clearly resolved in electron density.
- **FALSE** = "non-binder", no crystallographic evidence of binding.

Statistical significance between binding scores for binders vs. non-binders was assessed using the **Mann–Whitney U test**.

---

## 📄 File contents

| Filename                         | Description 
|----------------------------------|-------------
| `All_Retrospective-97.csv`       | Full corrected dataset (all poses).
| `Lateral_Retrospective-97.csv`   | Subset of compounds evaluated in lateral pose.
| `Diving_Retrospective-97.csv`    | Subset of compounds evaluated in diving pose.

Each file contains three columns:

| Column   | Description                                
|----------|--------------------------------------------
| `Name`   | Internal compound identifier               
| `Smiles` | Molecular SMILES representation            
| `Binding`| Corrected crystallographic outcome: TRUE or FALSE    

---

## 🔁 Usage context

- These files serve to assess quantify the level of noise in the uncorrected `OriginalRefined-957` dataset, and to validate the reliability of SAR models derived from crude reaction mixtures.
- These files also provide the **experimental ground truth**, or **test data**, used for evaluating model performance.
