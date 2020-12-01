import numpy as np
import pandas as pd

data = pd.read_csv(filepath_or_buffer='default of credit card clients.csv', sep=';', header=0)
## Business Understanding
# What is the average credit of defaulters vs non defaulters?
credit_def = data[data['default payment next month'] == 1]['LIMIT_BAL']
credit_nondef = data[data['default payment next month'] == 0]['LIMIT_BAL']
print("The mean credit limit of defaulters is {:.2f} and of non defaulters is {:.2f}".format(credit_def.mean(), credit_nondef.mean()))

# What is the percentage of male defaulters?
male_percents = data[data['SEX'] == 1]['default payment next month'].value_counts(normalize=True) * 100
print("{:.2f}% of men are defaulters".format(male_percents[1]))

# What is the percentage of female defaulters?
female_percents = data[data['SEX'] == 2]['default payment next month'].value_counts(normalize=True) * 100
print("{:.2f}% of women are defaulters".format(female_percents[1]))

# What is the scolarity of defaulters?
scolarity_percents =  data[data['default payment next month'] == 1]['EDUCATION'].value_counts(normalize=True) * 100
print("{:.2f}% of graduates, {:.2f}% of postgraduates and {:.2f}% of those with high school are defaulting".format(scolarity_percents[2], scolarity_percents[1], scolarity_percents[3]))

# What is the percentage of married defaulters?
married_percents = data[data['MARRIAGE'] == 1]['default payment next month'].value_counts(normalize=True) * 100
print("{:.2f}% of married people are defaulters".format(married_percents[1]))

# What is the percentage of single defaulters?
single_percents = data[data['MARRIAGE'] == 2]['default payment next month'].value_counts(normalize=True) * 100
print("{:.2f}% of single people are defaulters".format(single_percents[1]))

# What is the average age of defaulters?
age_def = data[data['default payment next month'] == 1]['AGE']
print("The mean age of defaulters is {:.2f} with a standard deviation of {:.2f}".format(age_def.mean(), age_def.std()))

## Data Understanding
# How many samples and features are in the data?
# How many features have incorrect data?


## Prepare Dat
# Fixing incorrect data


## Model Data
# KNN
# Decision Tree
# Random Forest
# MLP
# Ensemble MLP
# Ensemble Classifiers


## Results
