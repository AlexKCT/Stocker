#Block 1
import pandas as pd

# 去除煩人的 warrning
import warnings
warnings.filterwarnings('ignore')

# 讀入series
df = pd.read_csv('Stocker/price.csv', index_col='date', parse_dates=['date'])
price = df.squeeze()
price.head()

