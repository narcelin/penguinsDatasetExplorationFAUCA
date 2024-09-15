# -*- coding: utf-8 -*-
"""penguinsDatasetExploration.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13FezyA2l9JBZ_09WW5yRVI433Dt0TCTI

# Task 1: Load the Dataset
"""

# Import libs
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Reading dataset
p_df = pd.read_csv('penguins.csv')
print(p_df.head())

"""# Task 2: Handling Missing Data"""

# Check for null data
print("Start of NULL values search \n")
print(p_df.isnull().any())
print("\nEnd NULL values search \n")

# Drop rows with any column having NA/null data
np_df = p_df.dropna()

# Check new dataframe for null values
print("Start of NULL values search \n")
print(np_df.isnull().any())
print("\nEnd NULL values search \n")

"""# Task 3: Summary Statistics"""

np_stats = np_df.describe()
print(np_stats)

print('\n 1)', np_df['species'].value_counts())
print('\n 2)', np_df['island'].value_counts())
print('\n 3)', np_df['sex'].value_counts())

"""# Task 3: Visualizing the Data"""

np_df_n = np_df.iloc[:, 2:6]
print(np_df_n.head())

sns.pairplot(np_df_n, hue='body_mass_g')

# Create subplots
fig, axes = plt.subplots(1, 3, figsize=(20, 5))

# Plot for species
np_df['species'].value_counts().plot(
    kind='bar', ax=axes[0], title='Species Distribution')

# Plot for island
np_df['island'].value_counts().plot(
    kind='bar', ax=axes[1], title='Island Distribution')

# Plot for sex
np_df['sex'].value_counts().plot(
    kind='bar', ax=axes[2], title='Sex Distribution')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()

"""# Task 5: Covariance Matrix for Numeric Attributes"""

# cov_matrix of num
D = np_df_n.to_numpy()
D_center = D - np.mean(D, axis=0)
cov_matrix = np.cov(D_center, rowvar=False)

print(cov_matrix)

# The value of covariance represents the
# strength in the relationship
# between those two attributes.
# For example Covariance between attribute 1 and 3 is 50.058
# which represents a strong relationship while the relationship between
# attribute 2 and 3 is -15.948 referencing a weak relationship between the two.

np_df_a = np_df.iloc[:, [0, 1, 6]]
print("\n\n", np_df_a)

np_df_a_encoded = pd.get_dummies(np_df_a)
print(np_df_a_encoded)

cov_np_df_a_encoded = np_df_a_encoded.cov()
print(cov_np_df_a_encoded)

# Correlation Matrix

corr_matrix = np_df_n.corr()
print(corr_matrix)

# Create a heatmap of the correlation matrix
plt.figure(figsize=(8, 6))  # Set the figure size
sns.heatmap(corr_matrix)
plt.title('Correlation Matrix Heatmap')
plt.show()
