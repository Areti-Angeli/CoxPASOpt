# Cox-PASNet Survival Analysis Workflow

This repository includes all files needed to run and interpret the Cox-PASNet model for survival analysis, using both empirical and Optuna-optimized hyperparameters. The workflow also includes SHAP-based feature importance and pathway enrichment analysis via GSEApy.

---

## Files Overview

### Model Scripts
- **empirical_surv_status_coxpasnet.py**  
  → Trains Cox-PASNet using only survival status as covariate with empirical hyperparameters.

- **optuna_surv_status_coxpasnet.py**  
  → Same as above, but with Optuna-tuned hyperparameters.

- **empirical_condition+survstatus_coxpasnet.py**  
  → Trains Cox-PASNet using both condition and survival status with empirical hyperparameters.

- **optuna_condition+survstatus_coxpasnet.py**  
  → Same as above, using Optuna for hyperparameter optimization.

### Data Files
- **TRAINING.xlsx**, **VALIDATION.xlsx**, **TEST.xlsx**  
  → Data splits used for training, validation, and testing the model.

- **entire_data.xlsx**  
  → Full dataset including.

- **pt.xlsx**  
  → Pathway mapping file (gene-to-pathway associations) used to build the pathway mask.
  

### Output Files (Generated After Model Training)

- **`lin_pred.csv`**  
  → Prognostic index for each sample. 

- **`pathway_node.csv`**  
  → Pathway activation scores for each patient.

---
