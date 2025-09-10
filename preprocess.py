def preprocess(df):
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['dayofweek'] = df['date'].dt.dayofweek
    df['is_promo'] = df['promotion'].apply(lambda x: 1 if x == 'Yes' else 0)
    return df
