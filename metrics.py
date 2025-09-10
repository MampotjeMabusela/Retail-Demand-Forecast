def get_kpis(df):
    total_sales = df['sales'].sum()
    avg_sales = df['sales'].mean()
    promo_uplift = df[df['promotion'] == 'Yes']['sales'].mean() - df[df['promotion'] == 'No']['sales'].mean()
    return total_sales, avg_sales, promo_uplift
