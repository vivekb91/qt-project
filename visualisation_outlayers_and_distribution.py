import pandas as pd

file_path = 'Pregnancy During the COVID-19 Pandemic.csv'
data = pd.read_csv(file_path)
summary_stats = data.describe()
categorical_variables = ['Household_Income', 'Maternal_Education', 'Delivery_Mode', 'NICU_Stay', 'Language']
summary_stats
