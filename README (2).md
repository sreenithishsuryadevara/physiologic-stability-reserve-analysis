# Physiologic Stability Reserve (PSR) Reproducibility Suite

[![Research Pillar 1](figures/Fig1_Biological_Correlation.png)](figures/Fig1_Biological_Correlation.png)
*Figure 1: Biological validation linking vital sign instability to invasive cellular oxygenation (n=152,469 labs).*

---

## 🚀 Key Performance: The ML-PSR Solution
Using non-linear Machine Learning (Gradient Boosting), we extracted the occult deterioration signal from standard hospital macro-vitals, achieving a predictive **AUC of 0.784**.

| Predictive Discrimination (ROC) | Algorithm Decision Drivers |
| :---: | :---: |
| ![ROC Curve](figures/Fig2_ML_PSR_ROC.png) | ![Importances](figures/Fig3_Feature_Importance.png) |

---

## 🧠 The Mechanism: The Detection Gap
The PSR identifies "Occult Physiological Exhaustion" by detecting the loss of adaptive complexity before overt macro-vital failure occurs.

![Mechanism](figures/Fig4_PSR_Mechanism.png)

---

## Instructions for Peer Reviewers
1. **Pillar 1 (Biological):** Spearman correlation between continuous variance and invasive labs.
2. **Pillar 2 (Linear):** Multivariable Cox Proportional Hazards and C-Index testing.
3. **Pillar 3 (Non-Linear):** Gradient Boosting ML-PSR architecture.

**Reproducibility:** Secure DUA datasets and execute `reproducible_research.py`.
