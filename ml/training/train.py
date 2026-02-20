import os
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set MLflow tracking URI (from env variable for flexibility)
MLFLOW_TRACKING_URI = os.getenv(
    "MLFLOW_TRACKING_URI",
    "http://mlflow.platform.svc.cluster.local:5000"
)

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.set_experiment("iris-classifier")

def main():

    # Load dataset
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    # Hyperparameters
    n_estimators = 100
    max_depth = 5

    with mlflow.start_run():

        # Log parameters
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)

        # Train model
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=42
        )
        model.fit(X_train, y_train)

        # Evaluate
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)

        # Log model artifact
        mlflow.sklearn.log_model(
            model,
            artifact_path="model",
            registered_model_name="iris-classifier"
        )

        print(f"Model accuracy: {accuracy}")


if __name__ == "__main__":
    main()
