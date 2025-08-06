# import pandas as pd 
# from sklearn.datasets import load_iris, fetch_california_housing
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt 

# # load dataset
# iris = load_iris()
# x = pd.DataFrame(iris.data, columns=iris.feature_names)
# y = iris.target

# # split train and test
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

# # train decision tree classifier
# clf = DecisionTreeClassifier(max_depth=3, random_state=42)
# clf.fit(x_train, y_train)

# # decision tree classifier
# y_pred = clf.predict(x_test)
# accuracy = accuracy_score(y_test, y_pred)

# # visualization
# plt.figure(figsize=(12,8))
# plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
# plt.title('Decision Tree - Iris classifiction')
# plt.tight_layout()
# plt.show()

# # cross-validation
# cv_score = cross_val_score(clf, x, y, cv=5)
# print(f'5 fold cross validation(iris): {cv_score}')
# print(f'Mean CV accuracy : {cv_score.mean():.2f}')


# -------------------use fetch_california_housing dataset ----------------------------------------
# import pandas as pd 
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt 

# # load dataset
# housing = fetch_california_housing()
# x = pd.DataFrame(housing.data, columns=housing.feature_names)
# y = housing.target

# # split train and test
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

# # train decision tree classifier
# clf = DecisionTreeClassifier(max_depth=3, random_state=42)
# clf.fit(x_train, y_train)

# # decision tree classifier
# y_pred = clf.predict(x_test)
# accuracy = accuracy_score(y_test, y_pred)

# # visualization
# plt.figure(figsize=(12,8))
# plot_tree(clf, feature_names=housing.feature_names, class_names=housing.target_names, filled=True)
# plt.title('Decision Tree - Calfornia housing classifiction')
# plt.tight_layout()
# plt.show()

# # cross-validation
# cv_score = cross_val_score(clf, x, y, cv=5)
# print(f'5 fold cross validation(Calfornia housing): {cv_score}')
# print(f'Mean CV accuracy : {cv_score.mean():.2f}')

import pandas as pd
import seaborn as sns 
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, plot_tree
from sklearn.metrics import accuracy_score, mean_squared_error
import matplotlib.pyplot as plt

# Load the California Housing dataset
california = fetch_california_housing()
x = pd.DataFrame(california.data, columns=california.feature_names)
y = california.target

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train Decision Tree Regressor
clf = DecisionTreeRegressor(max_depth=3, random_state=42)
clf.fit(x_train, y_train)

# Predict and evaluate
y_pred = clf.predict(x_test)
mse = mean_squared_error(y_test, y_pred)

# Visualize
plt.figure(figsize=(16, 10))
plt.title('Decision Tree - California Housing')
plot_tree(clf, feature_names=california.feature_names, filled=True)
plt.tight_layout()
plt.show()

# Cross Validation
cv_scores = cross_val_score(clf, x, y, cv=5, scoring='neg_mean_squared_error')
print(f"5 Fold CV (MSE scores): {cv_scores}")
print(f"Mean CV MSE: {cv_scores.mean():.2f}")