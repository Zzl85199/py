import os
import pandas as pd
from scipy.io import savemat

# 定義函數處理檔案
def process_files(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # 如果是 .sav 檔案
            if file.lower().endswith('.sav'):
                try:
                    # 讀取 .sav 檔案
                    data = pd.read_spss(file_path)
                    
                    # 儲存為 .csv
                    csv_path = os.path.splitext(file_path)[0] + '.csv'
                    data.to_csv(csv_path, index=False)
                    print(f"Saved {csv_path}")

                    # 儲存為 Excel
                    excel_path = os.path.splitext(file_path)[0] + '.xlsx'
                    data.to_excel(excel_path, index=False)
                    print(f"Saved {excel_path}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

            # 如果是 Excel 檔案
            elif file.lower().endswith(('.xls', '.xlsx')):
                try:
                    # 讀取 Excel 檔案
                    data = pd.read_excel(file_path)
                    
                    # 儲存為 .sav
                    sav_path = os.path.splitext(file_path)[0] + '.sav'
                    savemat(sav_path, {'data': data.to_dict("list")})
                    print(f"Saved {sav_path}")

                    # 儲存為 .csv
                    csv_path = os.path.splitext(file_path)[0] + '.csv'
                    data.to_csv(csv_path, index=False)
                    print(f"Saved {csv_path}")
                except Exception as e:
                    print(f"Error processing {file}: {e}")

# 指定資料夾路徑
folder_path = "D:\SEM002700\Ch17"

# 執行函數
process_files(folder_path)
