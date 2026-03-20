# Physiologic Stability Reserve (PSR) Reproducibility Suite

This repository contains the complete 3-Pillar validation pipeline for the manuscript: 
**"Non-Linear Machine Learning Extraction of Physiologic Stability Reserve Outperforms Standard Linear Monitoring."**

## The 3-Pillar Validation Framework
1. **Pillar 1 (Biological):** Spearman correlation between continuous variance and invasive labs.
2. **Pillar 2 (Linear):** Multivariable Cox Proportional Hazards and C-Index testing.
3. **Pillar 3 (Non-Linear):** Gradient Boosting ML-PSR architecture.

## Instructions for Peer Reviewers
1. Ensure all dependencies are installed: `pip install -r requirements.txt`.
2. To maintain patient privacy (HIPAA), raw datasets are not included. Please refer to the manuscript for Data Use Agreement (DUA) request details.
3. Once datasets are secured, execute `reproducible_research.py` to replicate the primary findings (Spearman rho, Cox coefficients, and ML AUC).
