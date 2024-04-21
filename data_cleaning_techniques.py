# -*- coding: utf-8 -*-
"""Data Cleaning Techniques.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1no1RprD-vTdFOOPuHcnNaMD9W5krCSAC
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("exp2_CountryAgeSalary.csv")

df

x = df.iloc[: , 0:3].values
y= df.iloc[: , -1].values

x

y

from sklearn.impute import SimpleImputer

"""# Strategy Mean"""

imputer = SimpleImputer(missing_values=np.NaN , strategy = 'mean')
x[: , 1:] = imputer.fit_transform(x[: , 1:])
print(x)

df.Age = imputer.fit_transform(df['Age'].values.reshape(-1 , 1))[: , 0]
df

df.Salary = imputer.fit_transform(df['Salary'].values.reshape(-1 , 1))[: , 0]
df

"""# Strategy Median"""

df=pd.read_csv("exp2_CountryAgeSalary.csv")

df

imputer_median = SimpleImputer(missing_values=np.NaN , strategy = 'median')

df.Age = imputer_median.fit_transform(df['Age'].values.reshape(-1 , 1))[: , 0]
df.Salary = imputer_median.fit_transform(df['Salary'].values.reshape(-1 , 1))[: , 0]
df

"""#Strategy Mode"""

df=pd.read_csv("exp2_CountryAgeSalary.csv")

df

imputer_mode = SimpleImputer(missing_values=np.NaN , strategy = 'mode')

df.Age = imputer_median.fit_transform(df['Age'].values.reshape(-1 , 1))[: , 0]
df.Salary = imputer_median.fit_transform(df['Salary'].values.reshape(-1 , 1))[: , 0]
df

"""#Strategy most frequent"""

df=pd.read_csv("exp2_CountryAgeSalary.csv")

df

imputer_freq = SimpleImputer(missing_values=np.NaN , strategy = 'most_frequent')

df.Age = imputer_freq.fit_transform(df['Age'].values.reshape(-1 , 1))[: , 0]
df.Salary = imputer_freq.fit_transform(df['Salary'].values.reshape(-1 , 1))[: , 0]
df

"""#Const"""

df=pd.read_csv("exp2_CountryAgeSalary.csv")

df

imputer_const = SimpleImputer(missing_values=np.NaN , strategy = 'constant'  , fill_value=99 )

df.Age = imputer_const.fit_transform(df['Age'].values.reshape(-1 , 1))[: , 0]
df.Salary = imputer_const.fit_transform(df['Salary'].values.reshape(-1 , 1))[: , 0]
df

"""#One hot Encoding

"""

one_hot_encoded = pd.get_dummies(df['Purchased'])

df_encoded = pd.concat([df, one_hot_encoded], axis=1)

df_encoded.drop('Purchased', axis=1, inplace=True)

print(df_encoded)

"""#Label Encoding"""

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

df_encoded['Country_encoded'] = label_encoder.fit_transform(df_encoded['Country'])

df_encoded