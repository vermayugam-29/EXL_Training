from sklearn.linear_model import LinearRegression
import pandas as pd
from matplotlib import pyplot as plt

#Step1 : create sample data
data = {
    'size_sqft' : [600,800,1000,1200,1500,1800,2000],
    'price' : [15,20,25,30,35,40,50]
}

df = pd.DataFrame(data)


#Step2 : prepare input(x) and output(y)
x = df[['size_sqft']]
y = df['price']


#Step3 : create and train model
model = LinearRegression()
model.fit(x, y)


#Step4 : predict the new house sizes
new_sizes = pd.DataFrame({
    'size_sqft' : [1300,1750,2100]
})
predicted_prices = model.predict(new_sizes)


#Step5 : Print the predictions
print('Predicted Prices :')

for size, price in zip(new_sizes['size_sqft'], predicted_prices):
    print(f'{size} sqft ====> ${int(price)}')


#Step6 : Visualize data / Plot relationship
plt.scatter(
    df['size_sqft'],
    df['price'],
    color = 'blue',
    label = 'Training Data'
)
plt.xlabel('Size in SQFT')
plt.ylabel('Price')
plt.title('Price V/S Size in sqft')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()