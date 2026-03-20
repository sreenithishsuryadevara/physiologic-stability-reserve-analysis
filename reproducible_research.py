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

def run_pillar_1_biological_plausibility(labs_path, mover_path):
    print("\n[PILLAR 1] Establishing Biological Plausibility...")
    labs = pd.read_csv(labs_path)
    mover = pd.read_csv(mover_path)
    
    # Merge on MRN to link continuous variance to invasive labs
    merged = pd.merge(mover, labs, on='MRN')
    
    # Spearman Correlation: SpO2_SD vs PaO2 Lab Value
    rho, p_val = spearmanr(merged['SpO2_SD'], merged['Observation Value'])
    print(f"Spearman Correlation (rho): {rho:.4f}")
    print(f"P-value: {p_val:.4e}")

def run_pillar_2_linear_failure(master_path, mover_path):
    print("\n[PILLAR 2] Testing Linear Predictive Utility...")
    master = pd.read_csv(master_path)
    mover = pd.read_csv(mover_path)
    
    df = pd.merge(mover, master[['MRN', 'Comorbidity_Count']], on='MRN').drop_duplicates('MRN')
    
    # Multivariable Cox Regression
    cph = CoxPHFitter()
    cox_df = df[['duration_h', 'event', 'SpO2_SD', 'Age', 'ASA_RATING_C', 'Comorbidity_Count']].dropna()
    cph.fit(cox_df, duration_col='duration_h', event_col='event')
    
    # C-Index Calculation
    c_index = concordance_index(cox_df['duration_h'], -cox_df['SpO2_SD'], cox_df['event'])
    
    print("Cox Proportional Hazards Summary:")
    print(cph.summary[['exp(coef)', 'p']])
    print(f"Linear C-Index: {c_index:.4f}")

def run_pillar_3_ml_psr_solution(master_path, mover_path):
    print("\n[PILLAR 3] Extracting Non-Linear PSR via Machine Learning...")
    master = pd.read_csv(master_path)
    mover = pd.read_csv(mover_path)
    
    df = pd.merge(mover, master[['MRN', 'Comorbidity_Count']], on='MRN').drop_duplicates('MRN')
    features = ['SpO2_Mean', 'SpO2_SD', 'Age', 'ASA_RATING_C', 'Comorbidity_Count']
    X = df[features]
    y = df['event']
    
    # Stratified 80/20 Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Train Gradient Boosting Classifier
    model = GradientBoostingClassifier(n_estimators=200, max_depth=5, learning_rate=0.05, random_state=42)
    model.fit(X_train, y_train)
    
    # AUC Evaluation on Unseen Data
    scores = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, scores)
    print(f"Machine Learning PSR AUC: {auc:.4f}")
    
    # Feature Importances
    importances = pd.DataFrame({'Feature': features, 'Importance': model.feature_importances_}).sort_values('Importance', ascending=False)
    print("\nFeature Importance Drivers:")
    print(importances.to_string(index=False))

if __name__ == "__main__":
    # In a local environment, uncomment these to run with your CSV files:
    # run_pillar_1_biological_plausibility('filtered_hypoxemia_labs.csv', 'final_mover_cox_validated.csv')
    # run_pillar_2_linear_failure('master_cohort_analysis.csv', 'final_mover_cox_validated.csv')
    # run_pillar_3_ml_psr_solution('master_cohort_analysis.csv', 'final_mover_cox_validated.csv')
    print("Research Pipeline Loaded. Ready for validation with DUA-cleared data.")
