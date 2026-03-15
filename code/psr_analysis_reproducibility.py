
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.duration.hazard_regression import PHReg

def run_analysis(data_path):
    df = pd.read_csv(data_path)
    
    # Preprocessing
    df['Low_Stability_Flag'] = (df['Stability_Group'] == 'Low Stability').astype(int)
    df['Status'] = 1 
    
    # Primary Cox Model
    X = df[['Low_Stability_Flag', 'Age', 'ASA_Rating']]
    model = PHReg(df['Hospital_LOS'], X, status=df['Status']).fit()
    
    print("--- Adjusted Hazard Ratios ---")
    print(np.exp(model.params))
    print("\n--- P-Values ---")
    print(model.pvalues)
    
    return model

if __name__ == "__main__":
    run_analysis('MOVER_PSR_Validation_Final.csv')
