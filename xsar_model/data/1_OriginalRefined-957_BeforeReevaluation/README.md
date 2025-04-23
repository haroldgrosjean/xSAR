# 📁 1_OriginalRefined-957_BeforeReevaluation

This folder contains the **OriginalRefined-957** dataset: a curated list of 957 fragment elaboration compounds tested in high-throughput X-ray crystallography as crude reaction mixtures (CRMs). This dataset represents the **initial, uncorrected crystallographic readout** prior to reevaluation and false negative identification.

---

## 📋 Dataset Description

The 957 compounds included here were selected based on:
1. **Successful synthesis**, confirmed by automated LC-MS analysis of crude reaction mixtures.
2. **High-quality crystallographic data**, producing interpretable electron density.

This filtered set was extracted from a larger initial compound list and is referred to in the manuscript as **OriginalRefined-957**.

Each compound was labeled with a binary outcome:
- **TRUE** = "binder" or "hit", clearly resolved in electron density.
- **FALSE** = "non-binder" or "non-hit", no crystallographic evidence of binding.

---

## 📄 File contents

| Filename                                             | Description 
|------------------------------------------------------|-------------
| `All_OriginalRefined-957_BeforeReevaluation.csv`     | Full curated dataset of 957 ligands (combined poses).
| `Lateral_OriginalRefined-957_BeforeReevaluation.csv` | Subset of compounds in lateral pose.
| `Diving_OriginalRefined-957_BeforeReevaluation.csv`  | Subset of compounds in diving pose.

Each file contains three columns:

| Column   | Description                                
|----------|--------------------------------------------
| `Name`   | Internal compound identifier               
| `Smiles` | Molecular SMILES representation            
| `Binding`| Crystallographic outcome: TRUE or FALSE    

---

## 🔁 Usage context

These files provide the **starting point for xSAR modeling and benchmarking**. In later steps:
- This dataset was used to create the `Retrospective-97` set for reevaluation via high-throughput X-ray crystallography in pure form
- The `Retrospective-97` compound binding labels were updated post-retesting.
- Compounds from the `Retrospective-97` set were removed from `OriginalRefined-957` to create training data.