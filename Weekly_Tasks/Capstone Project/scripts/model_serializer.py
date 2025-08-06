import pickle

def save_model(model,acc, precision, recall, cm, f1):
    with open('model/churn_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    with open("model/model_metrics.txt", "w") as f:
        f.write("Model Evaluation Metrics:\n")
        f.write(f"Accuracy : {acc:.4f}\n")
        f.write(f"Precision: {precision:.4f}\n")
        f.write(f"Recall   : {recall:.4f}\n")
        f.write(f"F1 Score : {f1:.4f}\n")
        f.write(f"\nConfusion Matrix:\n{cm}\n")

def get_model():
    with open("model/churn_model.pkl", "rb") as f:
        model = pickle.load(f)

    return model