import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load and prepare data
df = pd.read_csv("sales_data.csv")
df_prophet = df[["Date", "Revenue"]].rename(columns={"Date": "ds", "Revenue": "y"})

# Create the model
model = Prophet()

# Fit the model to your data
model.fit(df_prophet)

# Make a future dataframe (next 7 days)
future = model.make_future_dataframe(periods=7)

# Forecast
forecast = model.predict(future)

# Show forecast
model.plot(forecast)
plt.title("📈 Revenue Forecast")
plt.xlabel("Date")
plt.ylabel("Predicted Revenue")
plt.tight_layout()
plt.show()
