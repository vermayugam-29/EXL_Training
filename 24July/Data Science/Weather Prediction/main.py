import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

#Step1 : Create dataset
data = {
    'Date': ['2025-07-25', '2025-07-26', '2025-07-27', '2025-07-28', '2025-07-29',
             '2025-07-30', '2025-07-31', '2025-08-01', '2025-08-02', '2025-08-03'],
    'Temperature': [29, 30, 32, 35, 33, 28, 27, 26, 25, 34],
    'Humidity': [70, 65, 60, 55, 67, 80, 85, 90, 75, 58],
    'WindSpeed': [12, 14, 13, 10, 9, 15, 16, 11, 10, 8],
    'Pressure': [1012, 1011, 1009, 1008, 1010, 1013, 1015, 1012, 1011, 1007],
    'Rain': ['No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}
df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

#Step2 : encoding

df['Rain'] = df['Rain'].map({'No' : 0, 'Yes' : 1})

#Step3 : train_set and target
train_set = ['Month', 'Day', 'Temperature', 'Humidity', 'WindSpeed', 'Pressure']
target = 'Rain'

x = df[train_set]
y = df[target]

#step4: model
model = LinearRegression()
model.fit(x, y)

#sample weather
sample_dates = ['2025-08-04', '2025-08-05', '2025-07-30', '2025-07-31']
samplenew_data = pd.DataFrame({
    'Month': [8, 8, 7, 7],
    'Day': [4, 5, 30, 31],
    'Temperature': [31, 35, 28, 27],
    'Humidity': [72, 50, 85, 88],
    'WindSpeed': [11, 9, 13, 15],
    'Pressure': [1010, 1008, 1013, 1014]
})

predicted_weather = model.predict(samplenew_data)

#printing
print('Predicted Weather :')
for date, pred in zip(sample_dates, predicted_weather):
    print(f"Date: {date} =>  {pred:.2f}")


# Predict on the training data
train_predictions = model.predict(x)

plt.plot(
    df['Date'],
    df['Rain'],
    label='Actual Rain',
    color='blue',
    marker='o'
)

plt.plot(
    df['Date'],
    train_predictions,
    label='Predicted Rain',
    color='red',
    marker='x',
    linestyle='--'
)

plt.xlabel('Date')
plt.ylabel('Rain (0 = No, 1 = Yes)')
plt.title('Actual vs Predicted Rain')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()