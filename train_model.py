from prophet import Prophet

def train_prophet(df):
    df = df.rename(columns={'date': 'ds', 'sales': 'y'})
    model = Prophet()
    model.fit(df)
    return model
