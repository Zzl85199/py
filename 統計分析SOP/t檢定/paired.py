import pandas as pd
from scipy.stats import ttest_rel, pearsonr

# 讀取 Excel 檔案
file_path = 'pair.xlsx'  # 替換為你的檔案名稱
data = pd.read_excel(file_path)

# 提取使用前 (Before) 和使用後 (After) 的分數
before_scores = data['Before']
after_scores = data['After']

# 成對樣本 t 檢定
t_stat, p_value = ttest_rel(before_scores, after_scores)

# 計算相關係數
correlation_coefficient, _ = pearsonr(before_scores, after_scores)

# 結果輸出
print(f"成對樣本 t 檢定結果：")
print(f"t 值 (t-statistic)：{t_stat:.3f}")
print(f"P 值 (p-value)：{p_value:.3f}")
print(f"使用前後分數的相關係數 (correlation coefficient)：{correlation_coefficient:.3f}")

# 解釋結果
if p_value < 0.05:
    print("\n結論：")
    print("P 值小於 0.05，表示在統計上有顯著差異，因此我們可以拒絕虛無假設，認為使用前後的印象分數有顯著差異。")
else:
    print("\n結論：")
    print("P 值大於或等於 0.05，表示在統計上沒有顯著差異，無法認為使用前後的印象分數有差異。")
    
print(f"此外，相關係數為 {correlation_coefficient:.3f}，顯示兩組數據的關聯程度。")
