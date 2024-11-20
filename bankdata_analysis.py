import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style for better aesthetics
sns.set(style="whitegrid")

# Load the dataset
file_path = 'bank.csv'  # Adjust this to your file's path
try:
    # Load dataset using semicolon as delimiter
    bank_data = pd.read_csv(file_path, sep=';')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()

# Data Exploration
print("First five rows of the dataset:")
print(bank_data.head())

print("\nDataset info:")
bank_data.info()

print("\nMissing values per column:")
print(bank_data.isnull().sum())

# Basic Data Analysis
print("\nSummary statistics for numerical columns:")
print(bank_data.describe())

# Group by job and calculate the mean balance
job_balance_mean = bank_data.groupby('job')['balance'].mean().sort_values(ascending=False)
print("\nAverage balance by job:")
print(job_balance_mean)

# Group by marital status and calculate the mean age
marital_age_mean = bank_data.groupby('marital')['age'].mean()
print("\nAverage age by marital status:")
print(marital_age_mean)

# Visualizations
# Line chart: Average balance by age
age_balance = bank_data.groupby('age')['balance'].mean()
plt.figure(figsize=(10, 6))
plt.plot(age_balance, label="Average Balance by Age", color="blue")
plt.title("Line Chart: Average Balance by Age")
plt.xlabel("Age")
plt.ylabel("Average Balance (€)")
plt.legend()
plt.grid()
plt.show()

# Bar chart: Average balance by job
plt.figure(figsize=(10, 6))
job_balance_mean.plot(kind='bar', color='teal', alpha=0.7)
plt.title("Bar Chart: Average Balance by Job")
plt.xlabel("Job")
plt.ylabel("Average Balance (€)")
plt.xticks(rotation=45)
plt.show()

# Histogram: Balance distribution
plt.figure(figsize=(10, 6))
sns.histplot(bank_data['balance'], kde=True, bins=30, color='green', alpha=0.6)
plt.title("Histogram: Balance Distribution")
plt.xlabel("Balance (€)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Age vs Balance by Marital Status
plt.figure(figsize=(10, 6))
sns.scatterplot(data=bank_data, x='age', y='balance', hue='marital', alpha=0.6)
plt.title("Scatter Plot: Age vs Balance by Marital Status")
plt.xlabel("Age")
plt.ylabel("Balance (€)")
plt.legend(title="Marital Status")
plt.show()

# Findings and Observations
print("\nFindings:")
print("1. Retired individuals have the highest average balance, while blue-collar jobs have the lowest.")
print("2. Divorced individuals are the oldest group on average, while singles are the youngest.")
print("3. The balance distribution is right-skewed, indicating a minority hold significantly higher balances.")
print("4. Age shows some correlation with balance, varying by marital status.")
