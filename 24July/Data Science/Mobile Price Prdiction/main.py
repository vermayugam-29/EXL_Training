#Predict mobile price based on camera quality and storage space
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

#Step1 : Create Data Set
data = {
    'storage' : [64, 128, 128, 256, 256, 512, 512],
    'camera' : [12, 12, 48, 48, 64, 64, 108],
    'price' : [300, 350, 400, 450, 500, 600, 700]
}

df = pd.DataFrame(data)

#Step 2 : Features and Target
x = df[['storage', 'camera']]
y = df['price']

#Step3 : Train the model
model = LinearRegression()
model.fit(x, y)

#Step4 : predict price for new phones
new_phones = pd.DataFrame({
    'storage' : [128, 256, 64],
    'camera' : [24, 64, 108]
})

predicted_price = model.predict(new_phones)

#Print Predictions
print('Predicted prices:')
for i, price in enumerate(predicted_price):
    print(f'Phone {i + 1}: Storage {new_phones.loc[i, 'storage']} GB,  '
          f'Camera {new_phones.loc[i, 'camera']} MP -> Price : ${int(price)}')

#Step6 : Visualize data / Plot relationship
plt.scatter(
    df['storage'],
    df['price'],
    color = 'blue',
    label = 'Training Data'
)
plt.xlabel('Storage')
plt.ylabel('Price')
plt.title('Price V/S Storage')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()