from scripts.model_serializer import get_model

def predict_model(sample_data, features):
    model = get_model()

    # Ensure the same column order
    sample_data = sample_data[features]

    predictions =  model.predict(sample_data)

    for i, pred in enumerate(predictions):
        print(f"Prediction for Customer {i + 1}: {pred}")
