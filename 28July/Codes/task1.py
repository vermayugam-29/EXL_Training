import pandas as pd  
import seaborn as sns 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,  cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt 

# # Load Data
# iris = load_iris()

# x = iris.data
# y = iris.target

# # splitting
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# # Modeling
# clf = DecisionTreeClassifier(random_state=42)
# clf.fit(x_train, y_train)

# # predict
# y_pred = clf.predict(x_test)

# acc = accuracy_score(y_test, y_pred)
# print("Iris Classification Accuracy:", acc)

# # Cross-validation
# cv_scores = cross_val_score(clf, x, y, cv=5)
# print("Cross-validation scores:", cv_scores)
# print("Mean CV Accuracy:", cv_scores.mean())

# # Visualize Decision Tree
# plt.figure(figsize=(10,6))
# plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
# plt.title("Decision Tree for Iris Classification")
# plt.show()

from sklearn.datasets import fetch_california_housing
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load California Housing dataset
california = fetch_california_housing()
X_california, y_california = california.data, california.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_california, y_california, test_size=0.2, random_state=42)

# Train Decision Tree Regressor
reg = DecisionTreeRegressor(random_state=42)
reg.fit(X_train, y_train)

# Predictions
y_pred = reg.predict(X_test)

# Evaluation Metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nCalifornia Housing Price Prediction:")
print("MSE:", mse)
print("MAE:", mae)
print("R2 Score:", r2)

# Cross-validation
cv_scores = cross_val_score(reg, X_california, y_california, cv=5, scoring='r2')
print("Cross-validation R2 scores:", cv_scores)
print("Mean CV R2:", cv_scores.mean())

# Optional: Visualize (shallow tree for clarity)
reg_small = DecisionTreeRegressor(max_depth=3, random_state=42)
reg_small.fit(X_train, y_train)

plt.figure(figsize=(12, 6))
plot_tree(reg_small, feature_names=california.feature_names, filled=True)
plt.title("Decision Tree for House Price Regression")
plt.show()
