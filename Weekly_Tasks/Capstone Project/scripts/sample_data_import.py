import pandas as pd

def import_sample_data():
    return pd.DataFrame([
    {
        'Age': 55,
        'Tenure': 8,
        'Balance': 150000.0,
        'NumOfProducts': 1,
        'HasCrCard': 1,
        'IsActiveMember': 0,
        'EstimatedSalary': 40000,
        'Gender': 'Female'
    },
    {
        'Age': 25,
        'Tenure': 1,
        'Balance': 0.0,
        'NumOfProducts': 4,
        'HasCrCard': 0,
        'IsActiveMember': 1,
        'EstimatedSalary': 100000,
        'Gender': 'Male'
    },
    {
        'Age': 40,
        'Tenure': 5,
        'Balance': 50000,
        'NumOfProducts': 2,
        'HasCrCard': 1,
        'IsActiveMember': 1,
        'EstimatedSalary': 70000,
        'Gender': 'Female'
    }
])
