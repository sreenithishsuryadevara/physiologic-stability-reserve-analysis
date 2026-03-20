import pandas as pd
import numpy as np
from scipy.stats import spearmanr
from lifelines import CoxPHFitter
from lifelines.utils import concordance_index
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
import warnings

warnings.filterwarnings('ignore')

def run_pillar_1_biological(labs_path, mover_path):
    print("\n[PILLAR 1] Biological Plausibility...")
    labs = pd.read_csv(labs_path)
    mover = pd.read_csv(mover_path)
    merged = pd.merge(mover, labs, on='MRN')
    rho, p_val = spearmanr(merged['SpO2_SD'], merged['Observation Value'])
    print(f"Spearman rho: {rho:.4f}, p-value: {p_val:.4e}")

def run_pillar_2_linear(master_path, mover_path):
    print("\n[PILLAR 2] Linear Predictive Failure...")
    master = pd.read_csv(master_path)
    mover = pd.read_csv(mover_path)
    df = pd.merge(mover, master[['MRN', 'Comorbidity_Count']], on='MRN').drop_duplicates('MRN')
    
    cph = CoxPHFitter()
    cox_df = df[['duration_h', 'event', 'SpO2_SD', 'Age', 'ASA_RATING_C', 'Comorbidity_Count']].dropna()
    cph.fit(cox_df, duration_col='duration_h', event_col='event')
    c_index = concordance_index(cox_df['duration_h'], -cox_df['SpO2_SD'], cox_df['event'])
    print(f"Linear C-Index: {c_index:.4f}\nVariance p-value: {cph.summary.loc['SpO2_SD', 'p']:.4f}")

def run_pillar_3_machine_learning(master_path, mover_path):
    print("\n[PILLAR 3A] ML-PSR Extraction...")
    master = pd.read_csv(master_path)
    mover = pd.read_csv(mover_path)
    df = pd.merge(mover, master[['MRN', 'Comorbidity_Count']], on='MRN').drop_duplicates('MRN')
    
    features = ['SpO2_Mean', 'SpO2_SD', 'Age', 'ASA_RATING_C', 'Comorbidity_Count']
    X = df[features]
    y = df['event']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = GradientBoostingClassifier(n_estimators=200, max_depth=5, learning_rate=0.05, random_state=42)
    model.fit(X_train, y_train)
    
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    print(f"ML-PSR AUC: {auc:.4f}")
    
def run_pillar_3_waveform_validation(rr_path):
    print("\n[PILLAR 3B] True PSR Waveform Validation...")
    rr_data = pd.read_csv(rr_path)
    results = []
    for patient_id, group in rr_data.groupby('Patient_ID'):
        rr_series = group['RR_Interval']
        mu = rr_series.mean()
        sigma = rr_series.std()
        rho_1 = rr_series.autocorr(lag=1)
        psr = (sigma / mu) ** (1 - rho_1)
        results.append({'Patient_ID': patient_id, 'Complexity': 1 - rho_1, 'True_PSR': psr})
    print(pd.DataFrame(results).to_string(index=False))

if __name__ == "__main__":
    print("Research Pipeline Loaded. Ready for validation with DUA-cleared datasets.")
