import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Load the uploaded Excel file to examine its structure
file_path_independence = 'independence.xlsx'
data_independence = pd.ExcelFile(file_path_independence)

# Display the sheet names to understand the file structure
data_independence.sheet_names

# Load the data from the first sheet
df_independence = data_independence.parse('Sheet1')

# Display the first few rows to understand its structure
df_independence.head()

# Create a pivot table for cross-tabulation of 'Sex' and 'Color' based on 'Sale'
cross_tab = pd.pivot_table(df_independence, values='Sale', index='Sex', columns='Color', aggfunc=np.sum, fill_value=0)

# Perform Chi-square test of independence
chi2_stat, p_value, dof, expected = chi2_contingency(cross_tab)

# Calculate percentage contribution table (Sex*Color proportion table)
percent_table = cross_tab / cross_tab.values.sum() * 100

# Display the results
print(cross_tab)
print(percent_table)
print("Chi square = ", chi2_stat)
print("p value = " , p_value)
