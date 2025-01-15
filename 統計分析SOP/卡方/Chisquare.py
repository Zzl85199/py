import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Load the uploaded Excel file to examine its structure
file_path_homogeneity = 'homogeneity.xlsx'
data_homogeneity = pd.ExcelFile(file_path_homogeneity)

# Display the sheet names to understand the file structure
data_homogeneity.sheet_names

# Load the data from the first sheet
df_homogeneity = data_homogeneity.parse('Sheet1')

# Display the first few rows to understand its structure
df_homogeneity.head()

# Create a pivot table for cross-tabulation of 'ID' and 'Opinion' based on 'number'
cross_tab_homogeneity = pd.pivot_table(
    df_homogeneity, 
    values='number', 
    index='ID', 
    columns='opinion', 
    aggfunc="sum",  # Use the string "sum" instead of np.sum
    fill_value=0
)


# Perform Chi-square test for homogeneity
chi2_stat_homogeneity, p_value_homogeneity, dof_homogeneity, expected_homogeneity = chi2_contingency(cross_tab_homogeneity)

# Calculate percentage contribution table (ID*Opinion proportion table)
percent_table_homogeneity = cross_tab_homogeneity / cross_tab_homogeneity.values.sum() * 100

# Display the results
print(cross_tab_homogeneity)
print(percent_table_homogeneity)
print("Chi square = " , chi2_stat_homogeneity)
print("p value = " , p_value_homogeneity)
