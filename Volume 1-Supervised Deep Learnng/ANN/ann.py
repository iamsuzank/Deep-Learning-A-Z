# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:44:39 2020

@author: Suzan
"""

#part 1-Data Preprocessing
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset=pd.read_csv('loan.csv')
X=dataset.drop(['Loan_ID','Loan_Status'],axis=1,inplace=True)
y=dataset['Loan_Status']
#X=dataset.iloc[:,1:12].values#input
#y=dataset.iloc[:,12].values#output

dataset.isnull().values.any()

#mean=dataset['Age'].median()
#inputs['Age']=inputs['Age'].fillna(mean)    
#Encoding Categorical Data
#Changing text data into numerical value
#There are 5 categories of data having value in string(Gender,Married,Education,Self_Employed,Property_Area)
#from sklearn.preprocessing import LabelEncoder,OneHotEncoder
#labelencoder_X_1=LabelEncoder()
#X[:,0]=labelencoder_X_1.fit_transform(X[:,0])

#spliting the dataset into train and test
#from sklearn.model_selection import train_test_split
#X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)

#feature scaling
#from sklearn.preprocessing import StandardScaler
#sc=StandardScaler()
#X_train=sc.fit_transform(X_train)
#X_test=sc.transform(X_test)