import pandas as pd
from scipy.stats import ttest_1samp

# 讀取上傳的Excel文件
file_path = 'Cost.xlsx'
data = pd.ExcelFile(file_path)

# 檢視文件中的表名
data.sheet_names

# 讀取第一個表格內容
df = data.parse(data.sheet_names[0])

# 假設家長給的平均生活費為6000
mean_allowance = 6000

# 單一樣本t檢定
t_stat, p_value = ttest_1samp(df['Cost'], mean_allowance)

# 計算單一變數的統計量（平均數、標準差及樣本數）
cost_stats = {
    '平均數': df['Cost'].mean(),
    '標準差': df['Cost'].std(),
    '樣本數': df['Cost'].count()
}

print('t=', t_stat)
print('p=', p_value)
