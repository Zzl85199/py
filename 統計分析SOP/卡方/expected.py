import pandas as pd
from scipy.stats import chisquare

# Load the uploaded Excel file to examine its structure
file_path = 'expected.xlsx'
data = pd.ExcelFile(file_path)

# Display the sheet names to understand the file structure
data.sheet_names

# Load the data from the first sheet
df = data.parse('Sheet1')

# Display the first few rows to understand its structure
df.head()

# Assuming the sales data represents the observed frequencies of different laptop colors
observed = df['Sale']

# Perform a chi-square goodness-of-fit test
# Assuming equal expected frequencies (uniform distribution) for initial analysis
expected = [observed.sum() / len(observed)] * len(observed)

# Calculate chi-square statistic and p-value
chi2_stat, p_value = chisquare(f_obs=observed, f_exp=expected)

print("Chi square = ", chi2_stat)
print("p value = ", p_value)