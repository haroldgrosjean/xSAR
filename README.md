# xSAR

**Crystallographic Structure-Activity-Relationship model from fragment elaboration in crude reaction mixtures**

---

## Overview

This repository accompanies the manuscript:  
**"A SAR model can be directly extracted from high-throughput crystallographic evaluation of fragment elaboration in crude reaction mixtures"**

It provides a rule-based framework to compute **Positive Binding Scores (PBS)** and **Negative Binding Scores (NBS)** for ligands tested in **crude reaction mixtures (CRMs)** via **X-ray crystallography**. These scores form the basis of the xSAR model, which aids retrospective analysis and prospective virtual screening in fragment-based drug discovery.

---

## Directory Structure

- `xsar_model/data/` – Input and out datasets used for model building, benchmarcking, virtual screening and experimental evaluation.
- `xsar_model/examples/` – Jupyter notebooks illustrating typical xSAR workflows.
- `xsar_model/scripts/` – Core pipeline logic for bit processing, scoring, and annotation.
- `xsar_model/conda_requirements.txt` – Full list of dependencies required to run the xSAR model.
- `LICENSE` – License under which the repository is distributed (MIT).
- `README.md` – This file.

---

## Installation

We recommend using `conda` to install dependencies in a controlled environment.

```bash
# Create and activate the environment
conda create --name xsar --file ./conda_requirements.txt
conda activate xsar
```

---

## Citation

TBD – Citation will be provided upon publication.

---

## Contact

For questions, suggestions, or collaborations, please reach out via the issues page.

---