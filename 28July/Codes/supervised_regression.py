# import pandas as pd  
# import seaborn as sns
# import matplotlib.pyplot as plt  
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression # continuous prediction for numbers
# from sklearn.metrics import mean_squared_error, r2_score

# tips = sns.load_dataset('tips')
# print(tips.head())

# x = tips[['total_bill']] # feature
# y = tips['tip'] # target

# # splitting training and testing
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# # create a model
# model = LinearRegression()

# # train a model
# model.fit(x_train, y_train)

# # prediction
# y_pred = model.predict(x_test)

# # evaluation
# mse = mean_squared_error(y_test, y_pred)
# re = r2_score(y_test, y_pred)
# print('Mean squared error = {mse:.2f}')
# print('R2 score = {r2:.2f}')

# plt.scatter(x_test, y_test, color='blue', label='Actual Tips')
# plt.plot(x_test, y_pred, color='red', linewidth=2, label = 'predicted tips')
# plt.xlabel('Total Bills')
# plt.ylabel('Tip')
# plt.title('Regrresion line: total bill vs tip')
# plt.tight_layout()
# plt.legend()
# plt.show()


import pandas as pd  
import seaborn as sns
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression # continuous prediction for numbers
from sklearn.metrics import mean_squared_error, r2_score

tips = sns.load_dataset('tips')
print(tips.head())

x = tips[['total_bill']] # feature
y = tips['size'] # target

# splitting training and testing
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# create a model
model = LinearRegression()

# train a model
model.fit(x_train, y_train)

# prediction
y_pred = model.predict(x_test)

# evaluation
mse = mean_squared_error(y_test, y_pred)
re = r2_score(y_test, y_pred)

print('Mean squared error = {mse:.2f}')
print('R2 score = {r2:.2f}')

plt.scatter(x_test, y_test, color='blue', label='actual size')
plt.plot(x_test, y_pred, color='red', linewidth=2, label = 'predicted size')
plt.xlabel('Total Bills')
plt.ylabel('size')
plt.title('Regrresion line: total bill vs size')
plt.tight_layout()
plt.legend()
plt.show()
