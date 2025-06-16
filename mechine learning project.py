import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("C:\\Users\\DELL\\Downloads\\Telegram Desktop\\hermanne1999.csv")
# Define input and output
x = df[['EN(MeV)']]
y = df['Renormalized CS(mB)']

# Polynomial regression model with scaling
model = make_pipeline(StandardScaler(), PolynomialFeatures(degree=4), LinearRegression())
model.fit(x, y)

# Predict user input
energy = float(input("Enter energy in MeV: \n"))
prediction = model.predict(pd.DataFrame({'EN(MeV)': [energy]}))
print(f"Predicted cross-section: {prediction[0]:.4f} millibarn")

# Check model performance
y_train_pred = model.predict(x)
r2 = r2_score(y, y_train_pred)
print(f"Model R² score: {r2:.4f}")

# Plot data and model fit
plt.scatter(x, y, color='blue', label='Actual Data')
x_range = np.linspace(x.min(), x.max(), 300).reshape(-1, 1)
y_pred = model.predict(x_range)
plt.plot(x_range, y_pred, color='red', label='Polynomial Fit (Degree 4)')
plt.xlabel('Energy (MeV)')
plt.ylabel('Cross-Section (mB)')
plt.title('Cross-Section Prediction with Polynomial Fit')
plt.legend()
plt.show()

