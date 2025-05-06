# 📁 5_virtual_screening

This folder contains the full compound selection data generated during the prospective virtual screening of the Enamine REAL database using the xSAR methodology. The procedure was applied independently for both the **lateral** and **diving** binding poses, and includes the application of 2D ligand-based filters (PBS, NBS), CoPriNet pricing, diversity selection, 3D docking and ΔΔG filtering, as well as final compound selection for experimental testing.

---

## 📋 Dataset Description

Each file corresponds to a step in the virtual screening pipeline for a given pose (`lateral` or `diving`):

1. **PBS-based filtering**  
   - Select top 45,000 compounds with highest PBS scores.  
   - Filter for lead-like physicochemical properties.  

2. **NBS-based filtering**  
   - Remove compounds with high NBS scores to exclude potential non-binders.  
   - Select most affordable 15,000 compounds using CoPriNet.  
   - Apply diversity selection (lazy MaxMin) to retain 10,000 diverse compounds.  

3. **Structure-based filtering with Fragmenstein**  
   - Compute compound poses using crystallographic ligand templates.  
   - Filter based on ligand energy ratio and select top 3% with lowest predicted ΔΔG values.  

4. **Final compound selection**  
   - Apply diversity filter on ΔΔG-ranked list.  
   - Select 47 compounds (lateral) and 46 compounds (diving), forming the **Prospective-93** set.

---

## 📄 File contents

| Filename                             | Description 
|--------------------------------------|-------------
| `1_PBS_selection_lateral.csv`        | Top PBS-scoring lateral compounds after initial filtering.
| `1_PBS_selection_diving.csv`         | Top PBS-scoring diving compounds after initial filtering.
| `2_NBS_selection_lateral.csv`        | PBS-filtered lateral compounds after NBS, pricing, and diversity filters.
| `2_NBS_selection_diving.csv`         | PBS-filtered diving compounds after NBS, pricing, and diversity filters.
| `3_fragmenstein_results_lateral.csv` | Fragmenstein docking results and energy scores for lateral pose.
| `3_fragmenstein_results_diving.csv`  | Fragmenstein docking results and energy scores for diving pose.
| `4_final_selection_lateral.csv`      | Final 47 selected lateral-scored compounds.
| `4_final_selection_diving.csv`       | Final 46 selected diving-scored compounds.

---

## 🧾 Column definitions

Below is a summary of key columns across the pipeline stages:

- `cid`: Enamine REAL Compound ID.
- `smiles`: SMILES string.
- `PBS`: Positive Binding Score (from crudes xSAR).
- `NBS`: Negative Binding Score (from crudes xSAR).
- `CoPriNet`: Predicted price from CoPriNet.
- `Experimental`: Flag for experimental eligibility.
- `RO5`, `RO3`: Rule-of-Five and Rule-of-Three compliance.
- `1st/2d/3d closest`: PDB ID to Tanimoto match to top 3 crystallised ligands.
- `ddg_0`, `ddg_1`, `ddg_2`: Predicted ΔΔG values from Fragmenstein (using 3 different templates).
- `energyRatio_0`, `energyRatio_1`, `energyRatio_2`: Ligand energy ratios relative to crystallised reference.
- `Mean ddG`, `Std ddG`, `Min ddG`: Summary ΔΔG metrics (final selection).
- `Mean ER`, `Std ER`, `Min ER`: Summary energy ratios (final selection).
- `Customer Code`: Internal compound name.
- `Tested`: Flag indicating experimental validation status.

---

## 🔁 Usage context

This dataset supports the **prospective evaluation of xSAR** for virtual screening and compound prioritisation. The pipeline demonstrates the use of xSAR-derived scores to guide both ligand-based and structure-based filtering of ultra-large libraries. Making full usage of the crystallographic readout. The final compound sets were purchased from Enamine and tested using high-throughput X-ray crystallography and GCI kinetic assays, as described in the manuscript.

