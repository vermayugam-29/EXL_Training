from scripts.data_normalize import normalize_data
from scripts.data_visualizations import perform_eda
from scripts.database import initialize_database
from scripts.data_loader import *
from scripts.data_cleaner import clean_data
from scripts.feature_engineering import features
from scripts.model_serializer import save_model
from scripts.model_training import model_train
from scripts.model_predict import predict_model
from scripts.sample_data_import import import_sample_data

pd.set_option('display.max_columns', None)

def main():

    initialize_database()
    upload_to_mysql('data/raw/exl_credit_card_churn_data.csv')
    df = load_data_from_sql()

    print('---------------------Initial Data Fetched from MySql---------------------')
    print(df.head(10))
    print('\nNull Values : \n', df.isnull().sum())
    print('\nInitial Info : \n', df.info())
    print('\nInitial Shape : ', df.shape)

    df = clean_data(df)

    print('---------------------Data After Cleaning---------------------')
    print(df.head(10))
    print('\nNull Values : \n', df.isnull().sum())
    print('\nInitial Info : \n', df.info())
    print('\nInitial Shape : ', df.shape)

    perform_eda(df.copy())

    df = features(df)
    df, scaler = normalize_data(df)

    print('---------------------Data After adding features and scaling---------------------')
    print(df.head(10))
    print('\nNull Values : \n', df.isnull().sum())
    print('\nInitial Info : \n', df.info())
    print('\nInitial Shape : ', df.shape)

    model, acc, precision, recall, cm, top_features, features_cols, f1 = model_train(df)

    save_model(model, acc, precision, recall, cm, f1)

    sample_data = import_sample_data()
    sample_data = features(sample_data)
    predict_model(sample_data, features_cols)


if __name__ == '__main__':
    main()