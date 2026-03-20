# Physiologic Stability Reserve (PSR) Analysis: A Tri-Pillar Validation Suite

![Research Pillar 1](figures/Fig1_Biological_Correlation.png)
*Figure 1: Biological validation linking continuous vital sign instability (SpO2 SD) to invasive cellular oxygenation nadir ($PaO_2$) using n=152,469 labs.*

---

## 🚀 Key Performance: The ML-PSR Solution
Using non-linear Machine Learning (Gradient Boosting), we extracted the occult deterioration signal from standard hospital macro-vitals, achieving a predictive **AUC of 0.784**.

| Predictive Discrimination (ROC Curve) | Clinical Decision Drivers |
| :---: | :---: |
| ![ROC Curve](figures/Fig2_ML_PSR_ROC.png) | ![Feature Importance](figures/Fig3_Feature_Importance.png) |

---

## 🧠 The Mechanism: The Detection Gap
The PSR identifies "Occult Physiological Exhaustion" by detecting the loss of adaptive complexity before overt macro-vital failure occurs. The mathematical mechanism is defined as:

$$PSR = \left(\frac{\sigma_{RR}}{\mu_{RR}}\right)^{1-\rho_1}$$

![Mechanism Comparison](figures/Fig4_PSR_Mechanism.png)
*Figure 4: The PSR captures the transition from high-complexity adaptation (Green) to pathological rigidity (Red) well before standard threshold alarms are triggered.*

---

## 🛠 Reproducibility Instructions
1. Clone this repository: `git clone https://github.com/sreenithishsuryadevara/physiologic-stability-reserve-analysis.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Secure DUA-cleared access to the MOVER, VitalDB, and CAST datasets.
4. Execute `reproducible_research.py` to replicate the primary findings.

**Contact:** sreenithish.vennnam@mnrmc.edu.in
