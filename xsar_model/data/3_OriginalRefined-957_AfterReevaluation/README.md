# 📁 3_OriginalRefined-957_AfterReevaluation

This folder contains the **OriginalRefined-957** dataset after the incorporation of corrected labels for the 97 compounds in the `Retrospective-97` subset. This updated dataset maintains the same 957 entries as the original `OriginalRefined-957_BeforeReevaluation` but includes refined binding outcomes for compounds that were re-purchased and manually re-evaluated by high-resolution X-ray crystallography.

---

## 📋 Dataset Description

The 957 compounds included here are identical to those in the OriginalRefined-957 dataset before reevaluation. However, for the 97 compounds belonging to the Retrospective-97 subset, the original labels have been **updated** based on:
1. **Purified resynthesis** and crystallographic reevaluation.
2. **Manual reassessment** of electron density for accurate binding classification.

Each compound is labeled with a binary outcome:
- **TRUE** = "binder", clearly resolved in electron density.
- **FALSE** = "non-binder", no crystallographic evidence of binding.

Only the 97 compounds from the Retrospective-97 subset have changed labels for identified false negatives; all others remain unchanged from the original dataset.

---

## 📄 File contents

| Filename                                            | Description 
|-----------------------------------------------------|-------------
| `All_OriginalRefined-957_AfterReevaluation.csv`     | Full updated dataset of 957 ligands (combined poses).
| `Lateral_OriginalRefined-957_AfterReevaluation.csv` | Subset of compounds in lateral pose.
| `Diving_OriginalRefined-957_AfterReevaluation.csv`  | Subset of compounds in diving pose.

Each file contains three columns:

| Column   | Description                                
|----------|--------------------------------------------
| `Name`   | Internal compound identifier               
| `Smiles` | Molecular SMILES representation            
| `Binding`| Crystallographic outcome: TRUE or FALSE    

---

## 🔁 Usage context

These files represent the **final, corrected label set**.  
They may serve as an improved dataset for future xSAR modelling.
