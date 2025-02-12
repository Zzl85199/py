import pandas as pd

# Load the Excel file to check its structure
file_path = 'Cost.xlsx'
data = pd.ExcelFile(file_path)

# Display sheet names to understand the structure of the file
data.sheet_names
# Load the data from the first sheet to examine its structure
df = data.parse('Sheet1')
df.head()
from scipy.stats import ttest_ind

# Filter data for male (1) and female (2)
male_data = df[df['Sex'] == 1]
female_data = df[df['Sex'] == 2]

# Perform independent sample t-tests for Score and Cost
score_ttest = ttest_ind(male_data['Score'], female_data['Score'], equal_var=True)
cost_ttest = ttest_ind(male_data['Cost'], female_data['Cost'], equal_var=True)

# Calculate means and standard deviations for Score and Cost
stats_summary = {
    "Metric": ["Score", "Cost"],
    "Male_Mean": [male_data['Score'].mean(), male_data['Cost'].mean()],
    "Male_StdDev": [male_data['Score'].std(), male_data['Cost'].std()],
    "Female_Mean": [female_data['Score'].mean(), female_data['Cost'].mean()],
    "Female_StdDev": [female_data['Score'].std(), female_data['Cost'].std()],
    "T_Value": [score_ttest.statistic, cost_ttest.statistic],
    "P_Value": [score_ttest.pvalue, cost_ttest.pvalue]
}

# Convert to DataFrame for better readability
stats_summary_df = pd.DataFrame(stats_summary)
print(stats_summary_df)
#import ace_tools as tools; tools.display_dataframe_to_user(name="男女學期成績與花費的T檢定結果", dataframe=stats_summary_df)
