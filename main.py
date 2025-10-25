import pandas as pd

def load_data(filepath):
    """Membaca dataset dari file CSV."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Membersihkan data dari duplikat dan nilai kosong."""
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df


import seaborn as sns
import matplotlib.pyplot as plt

def plot_sales_by_category(df, category_col, sales_col):
    """Membuat grafik total penjualan per kategori."""
    plt.figure(figsize=(8,5))
    sns.barplot(x=category_col, y=sales_col, data=df, estimator=sum)
    plt.title('Total Sales per Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
