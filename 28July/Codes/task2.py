import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# # load dataset
# iris = load_iris()

# x = pd.DataFrame(iris.data, columns=iris.feature_names)
# y = iris.target

# # splitting
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# # modeling
# clf = DecisionTreeClassifier(max_depth=3, random_state=42)
# clf.fit(x_train, y_train)

# # predict
# y_pred = clf.predict(x_test)

# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy Score:", accuracy)

# # 5-fold cross-validation accuracy
# cv_scores = cross_val_score(clf, x, y, cv=5)
# print("5-Fold CV Accuracy Scores:", cv_scores)
# print("Mean CV Accuracy:", cv_scores.mean())

# # Visualize the decision tree
# plt.figure(figsize=(12, 8))
# plot_tree(clf, feature_names=iris.feature_names,
#           class_names=iris.target_names, filled=True)
# plt.title("Decision Tree - Iris Classification")
# plt.show()


# ---------------------------------------------------------------------

# Part B - Decision Tree Regression on California Housing Dataset

from sklearn.datasets import fetch_california_housing
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load California housing data
housing = fetch_california_housing()
x = pd.DataFrame(housing.data, columns=housing.feature_names)
y = housing.target

# Split into train and test (80%-20%)
x_train_h, x_test_h, y_train_h, y_test_h = train_test_split(
    x, y, test_size=0.2, random_state=42)

# Initialize and train model
regressor = DecisionTreeRegressor(max_depth=4, random_state=42)
regressor.fit(x_train_h, y_train_h)

# Predict on test set
y_pred_h = regressor.predict(x_test_h)

# Evaluation metrics
mse = mean_squared_error(y_test_h, y_pred_h)
mae = mean_absolute_error(y_test_h, y_pred_h)
r2 = r2_score(y_test_h, y_pred_h)

print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("R2 Score:", r2)

# 5-fold CV scores (negative MSE)
cv_scores_reg = cross_val_score(regressor, x, y, cv=5, scoring='neg_mean_squared_error')
print("5-Fold CV Negative MSE Scores:", cv_scores_reg)
print("Mean CV Negative MSE:", cv_scores_reg.mean())

# Visualize the regression tree
plt.figure(figsize=(16, 10))
plot_tree(regressor, feature_names=housing.feature_names, filled=True, max_depth=2)
plt.title("Decision Tree - California Housing Regression")
plt.show()
