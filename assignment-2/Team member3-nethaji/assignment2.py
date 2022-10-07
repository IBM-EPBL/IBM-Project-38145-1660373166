# -*- coding: utf-8 -*-
"""assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dL-RISaTSXUudt_90GDDQK4zhvJtRfth
"""

import numpy as np 
import pandas as pd

df = pd.read_csv("Churn_Modelling.csv")
df

"""Visualization"""

import matplotlib.pyplot as plt
import seaborn as sns

"""Univariate Analysis"""

df.dtypes

plt.scatter(df.index,df['Age'])
plt.show()

"""Bivariate analysis"""

sns.boxplot(x='Gender',y='Age',data=df)
plt.show()

sns.barplot(x='Gender',y='Exited',data=df)
sns.countplot(x='Gender',data=df)

"""Multi variate analysis"""

g=sns.PairGrid(df)
g.map(sns.scatterplot)
g

"""Descriptive analysis"""

df = pd.DataFrame(df)
df

df.describe()

df.count()

df['Geography'].value_counts()

df.isnull().sum()

df.isna().any()

plt.scatter(df.index,df['Balance'])
plt.show()

sns.scatterplot(x=df.index,y=df['Balance'],hue=df['NumOfProducts'])

sns.barplot(x='Gender',y='Exited',data=df)
sns.countplot(x='Gender',data=df)

sns.boxplot(x='CreditScore', data=df)

x=df.iloc[:,:-1].values
y=df.iloc[:,4].values
print(x,y)

from sklearn.model_selection import train_test_split
training_data,testing_data=train_test_split(df,test_size=1,random_state=3)
print(training_data,testing_data)