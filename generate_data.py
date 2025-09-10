import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate 280 days of dates
dates = [datetime.today() - timedelta(days=i) for i in range(280)]
dates.reverse()

# Simulate seasonal sales patterns
base_sales = np.sin(np.linspace(0, 3 * np.pi, 280)) * 50 + 200
noise = np.random.normal(0, 20, 280)
sales = (base_sales + noise).astype(int)

# Simulate promotional activity
promotion = np.random.choice(['Yes', 'No'], size=280, p=[0.3, 0.7])

# Build DataFrame
df = pd.DataFrame({
    'date': dates,
    'sales': sales,
    'promotion': promotion
})

# Save to CSV
df.to_csv('data/sales_data.csv', index=False)
print("✅ sales_data.csv with 280 days generated successfully!")
