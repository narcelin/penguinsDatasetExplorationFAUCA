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
p_df.head()

"""# Task 2: Handling Missing Data"""

# Check for null data
p_df.isnull().any()

# Drop rows with any column having NA/null data
np_df = p_df.dropna()

# Check new dataframe for null values
np_df.isnull().any()

"""# Task 3: Summary Statistics"""

np_stats = np_df.describe()
print(np_stats)

print('\n 1)', np_df['species'].value_counts())
print('\n 2)', np_df['island'].value_counts())
print('\n 3)', np_df['sex'].value_counts())

"""# Task 3: Visualizing the Data"""

sns.pairplot(np_df, hue='species')

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

# Computing covariance matrix for all numeric attribute
numeric_df = np_df.select_dtypes(include=['number'])
numeric_df
# covariance_matrix = numeric_df.cov()
# covariance_matrix
