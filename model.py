# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:45:32 2020

@author: Gowrav Tata
"""

import os 
os.chdir(r'C:\Users\Gowrav Tata\Data Science\test\titanic')
import pandas as pd
from sklearn.linear_model import LogisticRegression
# create df
train = pd.read_csv('titanic.csv') # change file path

# drop null values
train.dropna(inplace=True)

# features and target
target = 'Survived'
    features = ['Pclass', 'Age', 'SibSp', 'Fare']

# X matrix, y vector
X = train[features]
y = train[target]

# model
model = LogisticRegression()
model.fit(X, y)
model.score(X, y)


import pickle
pickle.dump(model,open('model.pkl','wb'))
print(model.predict([[2, 9, 0,18]]))

