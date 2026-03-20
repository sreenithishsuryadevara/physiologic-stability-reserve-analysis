# Data Dictionary: PSR Research Cohort

| Variable Name | Description | Source | Units |
| :--- | :--- | :--- | :--- |
| **MRN** | De-identified Medical Record Number | Institutional | ID String |
| **SpO2_Mean** | Mean peripheral oxygen saturation over surgical duration | Vital Signs | % |
| **SpO2_SD** | Standard deviation of SpO2 (Continuous Variance) | Vital Signs | % |
| **Age** | Patient age at time of admission | Demographics | Years |
| **ASA_RATING_C** | ASA Physical Status Classification (1-5) | Clinical | Numeric |
| **Comorbidity_Count** | Sum of pre-existing ICD-10 comorbidities | EMR | Count |
| **Observation Value**| Invasive PaO2 (Arterial Blood Gas) | Labs | mmHg |
| **event** | Primary Endpoint (Unplanned ICU/Intubation) | Clinical | 0/1 |
| **duration_h** | Time from intubation to event or censoring | Clinical | Hours |
| **RR_Interval** | Beat-to-beat normal-to-normal intervals (CAST Cohort) | EKG | ms |
