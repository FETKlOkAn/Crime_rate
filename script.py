import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Load the CSV file
data = pd.read_csv('analysis-public-place-assaults-sexual-assaults-and-robberies-2015-csv.csv')

# Strip leading/trailing whitespaces from column names
data.columns = data.columns.str.strip()

# Strip leading/trailing spaces and replace non-numeric values like '-' or empty strings
data['Rate_per_10000_population'] = data['Rate_per_10000_population'].str.strip()  # Remove leading/trailing spaces
data['Rate_per_10000_population'] = data['Rate_per_10000_population'].replace({'-': '0', '': '0'})  # Replace '-' and empty strings with '0'
data['Rate_per_10000_population'] = data['Rate_per_10000_population'].replace(',', '', regex=True)  # Remove commas
data['Rate_per_10000_population'] = pd.to_numeric(data['Rate_per_10000_population'], errors='coerce')  # Convert to float, set errors to NaN

# Calculate the national average victimization rate
national_avg_rate = data['Rate_per_10000_population'].mean()

# Add a column to indicate if the rate is above the national average
data['Above_National_Average'] = data['Rate_per_10000_population'] > national_avg_rate

# Filter data to include only areas with rates above the national average
filtered_data = data[data['Above_National_Average']]
filtered_data2 = data[data['Rate_per_10000_population'] > 1000]
# Find areas with the highest victimization rates among those above the national average
highest_rates = filtered_data.sort_values(by='Rate_per_10000_population', ascending=False)

# Calculate the 75th percentile for the victimization rate
quantile_75th = np.quantile(data['Rate_per_10000_population'].dropna(), 0.75)

# Divide the data into two groups: above and below the national average
above_avg = data[data['Rate_per_10000_population'] > national_avg_rate]['Rate_per_10000_population']
below_avg = data[data['Rate_per_10000_population'] <= national_avg_rate]['Rate_per_10000_population']

# Perform a two-sample t-test
t_stat, p_value = stats.ttest_ind(above_avg.dropna(), below_avg.dropna(), equal_var=False)

# Output the results
print(f'T-test statistic: {t_stat:.4f}')
print(f'P-value: {p_value:.4f}')

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in victimization rates.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in victimization rates.")

# Print the areas with the highest rates above the national average
print("Areas with Victimization Rates Above the National Average:")
print(highest_rates[['Area_unit_2013_label', 'Rate_per_10000_population']])

# Plot the victimization rates for areas above the national average
plt.figure(figsize=(12, 6))
plt.bar(filtered_data2['Area_unit_2013_label'], filtered_data2['Rate_per_10000_population'], color='red')
plt.axhline(y=quantile_75th, color='green', linestyle='--', label=f'75th Percentile: {quantile_75th:.2f}')
plt.xticks(rotation=90, fontsize=8)
plt.xlabel('Area')
plt.ylabel('Victimization Rate per 10,000 Population')
plt.title('Victimization Rate Comparison for Areas Above the National Average')
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
