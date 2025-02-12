import pandas as pd
from scipy.stats import f_oneway
import numpy as np

# Load the Excel file to check its content
file_path = 'Cost.xlsx'
data = pd.ExcelFile(file_path)

# Display sheet names to understand the structure of the file
print("Sheet Names:", data.sheet_names)

# Load the data from the first sheet
df = data.parse('Sheet1')

# Display the first few rows of the dataset to understand its structure
print(df.head())

# Grouping data by gender (Sex)
grouped = df.groupby('Sex')

# Calculating means, standard deviations, and counts
stats = grouped.agg(
    Mean_Score=('Score', 'mean'),
    Std_Score=('Score', 'std'),
    Count_Score=('Score', 'count'),
    Mean_Cost=('Cost', 'mean'),
    Std_Cost=('Cost', 'std'),
    Count_Cost=('Cost', 'count')
).reset_index()

# Display the calculated statistics
print("\nGrouped Statistics (Mean, Std, Count):")
print(stats)

# Performing ANOVA for Score and Cost based on Sex
anova_score = f_oneway(
    df[df['Sex'] == 1]['Score'],
    df[df['Sex'] == 2]['Score']
)

anova_cost = f_oneway(
    df[df['Sex'] == 1]['Cost'],
    df[df['Sex'] == 2]['Cost']
)

# Summarizing results in tables
anova_summary = {
    "Variable": ["Score", "Cost"],
    "F-Statistic": [anova_score.statistic, anova_cost.statistic],
    "P-Value": [anova_score.pvalue, anova_cost.pvalue]
}

anova_df = pd.DataFrame(anova_summary)

# Display the ANOVA results
print("\nANOVA Results:")
print(anova_df)
