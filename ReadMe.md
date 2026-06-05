# Iris Flower Classification Using Neural Network

## Project Overview

This project is a Neural Network-based classification system developed using Python and Scikit-learn. The model is trained on the Iris dataset and predicts the species of a flower based on its sepal and petal measurements.

The system uses a Multi-Layer Perceptron (MLP) Neural Network to classify flowers into one of three categories:

* Setosa
* Versicolor
* Virginica

---

## Objectives

* Learn the basics of Neural Networks.
* Understand data classification techniques.
* Practice machine learning using Python.
* Perform data preprocessing and feature scaling.
* Evaluate model performance using different metrics.

---

## Features

### Dataset Loading

* Loads the Iris dataset from Scikit-learn.

### Data Preprocessing

* Feature scaling using StandardScaler.
* Training and testing data split.

### Neural Network Training

* Uses MLPClassifier.
* Trains a Neural Network with hidden layers.

### Model Evaluation

* Accuracy Score
* F1 Score
* Confusion Matrix
* Classification Report

### Flower Prediction

Users can enter:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The model predicts the flower species and displays prediction probabilities.

---

## Technologies Used

* Python 3
* Scikit-learn
* Visual Studio Code (VS Code)
* GitHub

---

## Project Structure

```text
Iris-Neural-Network/
│
├── iris_classification.py
├── README.md
└── requirements.txt
```

### File Description

#### iris_classification.py

Contains dataset loading, preprocessing, model training, evaluation, and prediction logic.

#### README.md

Contains project documentation and instructions.

#### requirements.txt

```txt
scikit-learn
```

---

## How the System Works

1. Load the Iris dataset.
2. Scale the features using StandardScaler.
3. Split data into training and testing sets.
4. Train the Neural Network model.
5. Evaluate model performance.
6. Accept user input.
7. Predict flower species.
8. Display prediction result and probabilities.

---

## Algorithm

1. Start the program.
2. Load Iris dataset.
3. Scale feature values.
4. Split dataset into training and testing data.
5. Train MLP Neural Network.
6. Test model performance.
7. Accept flower measurements from user.
8. Predict flower species.
9. Display results.
10. End program.

---

## Sample Output

```text
Total Samples: 150
Classes: ['setosa' 'versicolor' 'virginica']

Accuracy: 100.0 %

Enter Sepal Length: 5.1
Enter Sepal Width: 3.5
Enter Petal Length: 1.4
Enter Petal Width: 0.2

Predicted Flower Type: setosa

Prediction Probabilities:
[[0.99 0.01 0.00]]
```

---

## Advantages

* Simple implementation of Neural Networks
* High prediction accuracy
* Easy to understand for beginners
* Uses a well-known dataset
* Demonstrates machine learning workflow

---

## Limitations

* Works only with the Iris dataset
* Small dataset size
* Requires numerical input values
* Limited to three flower classes

---

## Conclusion

This project demonstrates how a Neural Network can be used for classification tasks. The model successfully learns patterns from the Iris dataset and predicts flower species based on user-provided measurements. It is an excellent beginner project for understanding machine learning and neural networks.

---

## Author

Muhammad Zeeshan

Computer Science Student
