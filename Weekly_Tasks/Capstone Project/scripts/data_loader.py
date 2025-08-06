import pandas as pd
from scripts.database import get_db_connection

def upload_to_mysql(file_path):
    df = pd.read_csv(file_path)

    conn = get_db_connection()
    cursor = conn.cursor()

    query = ("""
        INSERT INTO customers (
            CustomerID, Gender, Age, Tenure, Balance,
            NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Churn
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            Gender = VALUES(Gender),
            Age = VALUES(Age),
            Tenure = VALUES(Tenure),
            Balance = VALUES(Balance),
            NumOfProducts = VALUES(NumOfProducts),
            HasCrCard = VALUES(HasCrCard),
            IsActiveMember = VALUES(IsActiveMember),
            EstimatedSalary = VALUES(EstimatedSalary),
            Churn = VALUES(Churn)
    """)

    for _, row in df.iterrows():
        cursor.execute(
            query, (
                row['CustomerID'] if pd.notna(row['CustomerID']) else None,
                row['Gender'].strip().lower() if pd.notna(row['Gender']) else None,
                safe_int(row['Age']),
                safe_int(row['Tenure']),
                float(row['Balance']) if pd.notna(row['Balance']) else None,
                safe_int(row['NumOfProducts']),
                safe_int(row['HasCrCard']),
                safe_int(row['IsActiveMember']),
                float(row['EstimatedSalary']) if pd.notna(row['EstimatedSalary']) else None,
                safe_int(row['Churn'])
            )
        )

    conn.commit()
    cursor.close()
    conn.close()
    print("Data uploaded successfully.")


def load_data_from_sql():
    try:
        conn = get_db_connection()

        query = "SELECT * FROM customers"
        df = pd.read_sql(query, conn)

        return df

    except Exception as e:
        print('Error:',e)
        return None
    finally:
        if conn.is_connected():
            conn.close()


def safe_int(value):
    if pd.isna(value):
        return None
    try:
        return int(float(value))
    except (ValueError, TypeError):
        value_str = str(value).strip().lower()
        if value_str in ['yes', 'true']:
            return 1
        elif value_str in ['no', 'false']:
            return 0
        else:
            return None