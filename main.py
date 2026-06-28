import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score

def run_classification_pipeline():
    print("==================================================")
    print("   DECODELABS SUPERVISED CLASSIFICATION PIPELINE  ")
    print("==================================================")
    
    # Step 1: Raw Material Ingestion (Load Iris Benchmark Dataset)
    iris = load_iris()
    X = iris.data  # Dimensions / Features: Sepal & Petal metrics
    y = iris.target  # Classes: Setosa (0), Versicolor (1), Virginica (2)
    
    print(f"[*] Dataset successfully loaded.")
    print(f"[*] Total balanced historical items: {X.shape[0]}")
    print(f"[*] Dimension features tracking: {iris.feature_names}")
    print(f"[*] Classification targets: {iris.target_names}\n")
    
    # Step 2: Structural Integrity (Shuffle & Train-Test Split)
    # Shuffling randomizes sequence layouts to erase natural collection pattern biases
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_split=0.3, random_state=42, stratify=y
    )
    print(f"[+] Pattern recognition layout (Training Set size): {X_train.shape[0]}")
    print(f"[+] Operational validation layout (Testing Set size): {X_test.shape[0]}\n")
    
    # Step 3: Gatekeeper Execution (Feature Standardization/Scaling)
    # Equalizes feature scale standard deviations (Mean=0, Var=1) to secure metric balance
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("[*] Feature scaling applied via StandardScaler (Mean = 0, Variance = 1).")
    
    # Step 4: Logic Skeleton Training (K-Nearest Neighbors Algorithm)
    k_value = 5
    knn_model = KNeighborsClassifier(n_neighbors=k_value)
    knn_model.fit(X_train_scaled, y_train)
    print(f"[+] Core structural logic trained using KNN Engine (k={k_value}).\n")
    
    # Step 5: Verification and Evaluation Matrix Metrics
    y_pred = knn_model.predict(X_test_scaled)
    
    accuracy = accuracy_score(y_test, y_pred)
    macro_f1 = f1_score(y_test, y_pred, average='macro')
    conf_matrix = confusion_matrix(y_test, y_pred)
    
    print("---------------- MODEL ASSESSMENT ----------------")
    print(f"Overall Algorithmic Accuracy : {accuracy * 100:.2f}%")
    print(f"Unified Validation Macro F1-Score: {macro_f1:.4f}")
    print("\n--- Confusion Matrix Matrix Structural Layout ---")
    print(conf_matrix)
    print("\n---------------- Detailed Classification Profile ----------------")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

if __name__ == "__main__":
    run_classification_pipeline()