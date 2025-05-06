# 📁 6_experimental_validation

This folder contains the **GCI assay results** for compounds selected from the prospective virtual screening campaign. Grating-Coupled Interferometry (GCI) was used to experimentally measure kinetic binding parameters for 93 compounds (Prospective-93) against PHIP(2). Assays were performed using the Creoptix® WAVE system with the WaveRAPID® injection scheme, and kinetic data were processed using the Direct Kinetics fitting engine.

---

## 📋 Dataset Description

Two datasets are provided:
1. A full set of kinetic results for all tested compounds.
2. A filtered set of hits meeting predefined criteria for kinetic quality and binding signal.

Binding was considered meaningful when:
- **ka and kd error < 25%**
- **Rmax > 10 pg/√mm**

Ligand efficiency (LE) was calculated for hit compounds to evaluate interaction efficiency normalised to heavy atom count.

---

## 📄 File contents

| Filename                  | Description |
|---------------------------|-------------|
| `1_GCI_results_all.csv`   | Raw kinetic binding results for all tested compounds. |
| `2_GCI_results_hits.csv`  | Filtered set of compounds meeting hit criteria (ka/kd error < 25%, Rmax > 10) and including computed ligand efficiency (LE). |

---

## 🧾 Column definitions

### Common to both files:
| Column                    | Description |
|---------------------------|-------------|
| `cid`                     | Enamine REAL Compound ID. |
| `smiles`                 | SMILES representation |
| `Ka (M-1s-1)`             | Association rate constant |
| `Ka error (%)`            | % error on Ka |
| `Ka error (M-1s-1)`       | Absolute error on Ka |
| `Kd (s-1)`                | Dissociation rate constant |
| `Kd error (%)`            | % error on Kd |
| `Kd error (s-1)`          | Absolute error on Kd |
| `KD (M)`                  | Dissociation equilibrium constant |
| `KD lower (M)`            | Lower bound of KD (M) |
| `KD upper (M)`            | Upper bound of KD (M) |
| `KD (uM)`                 | KD in micromolar |
| `KD lower (uM)`           | Lower bound in μM |
| `KD upper (uM)`           | Upper bound in μM |
| `Rmax (pg/sqrt(mm))`      | Maximum binding response signal |
| `Sqrt(Chi2) (pg/sqrt(mm))`| Root Chi-squared error on fit |
| `MW`                      | Molecular weight |
| `Crystal Binding`         | TRUE/FALSE crystallographic binding confirmation |
| `Customer Code`           | Internal compound name|

### Additional in `2_GCI_results_hits.csv` only:
| Column    | Description |
|-----------|-------------|
| `LE`      | Ligand efficiency in kcal/(mol·heavy atom) |

---

## 🔁 Usage context

These files provide experimental validation of compounds selected through xSAR-guided virtual screening. The data support:
- Assessment of hit rate and kinetic quality of selected virtual screening compounds.
- Classification of follow-up compounds as kinetic hits based on binding parameters
