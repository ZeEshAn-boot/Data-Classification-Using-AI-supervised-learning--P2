from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score

# Load Dataset (Input Phase)

iris = load_iris()
X = iris.data
y = iris.target

print("Total Samples:", len(X))
print("Classes:", iris.target_names)

# Feature Scaling (Gatekeeper Rule)

# StandardScaler establishes: Mean = 0, Variance = 1

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split (Structural Integrity)
# Shuffling removes order bias before splitting into an 80/20 breakdown
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

#  Neural Network Model (Process Phase)

# Instantiating a multi-layer network structure with two hidden layers of 10 neurons each

model = MLPClassifier(
    hidden_layer_sizes=(10, 10),
    activation='relu',
    max_iter=1000,
    random_state=42
)

# Training  
model.fit(X_train, y_train)



#  Evaluation (Output Phase)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
cm = confusion_matrix(y_test, y_pred)

print("\n===== MODEL EVALUATION =====")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("F1 Score:", round(f1, 4))
print("Confusion Matrix:\n", cm)
print("\nClassification Report:\n", classification_report(y_test, y_pred))


#  Live User Input Prediction
print("\n===== NEW FLOWER PREDICTION =====")

sepal_length = float(input("Enter Sepal Length (cm): "))
sepal_width  = float(input("Enter Sepal Width (cm): "))
petal_length = float(input("Enter Petal Length (cm): "))
petal_width  = float(input("Enter Petal Width (cm): "))

new_flower = [[sepal_length, sepal_width, petal_length, petal_width]]

# Crucial step: Scale the user input coordinates identically to the historical data
new_flower_scaled = scaler.transform(new_flower)

# Make prediction using the trained neural connections
prediction = model.predict(new_flower_scaled)
probabilities = model.predict_proba(new_flower_scaled)

print("\nPredicted Flower Type:", iris.target_names[prediction][0])
print("Prediction Probabilities across classes:", probabilities)