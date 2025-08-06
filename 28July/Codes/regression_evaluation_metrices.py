from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

y_true = [100, 200, 300]
y_pred = [90, 210, 310]

mse = mean_squared_error(y_true, y_pred)
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)

print(f'Mean squared error: {mse:.2f}')
print(f'Mean Absolute error: {mae:.2f}')
print(f'R2 score: {r2:.2f}')