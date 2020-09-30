import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def pre_data():
    df = pd.read_csv('train.csv')
    df = df.drop('Cabin',axis=1)
    mean_age = round(df['Age'].mean())
    df['Age'].fillna(mean_age,inplace=True)
    df['Embarked'].value_counts()
    df['Embarked'].fillna('S',inplace=True)
    dummies_embarked = pd.get_dummies(df['Embarked'],drop_first=True)
    df = pd.concat([df.drop('Embarked',axis=1),dummies_embarked],axis=1)
    df = df.drop('Name',axis=1)
    male_dummies = pd.get_dummies(df['Sex'],drop_first=True)
    df = pd.concat([df.drop('Sex',axis=1),male_dummies],axis=1)
    df = df.drop('Ticket',axis=1)
    return df
pre_data()
#Train
from sklearn.model_selection import train_test_split
X = df.drop('Survived',axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01)
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
pred = logmodel.predict(X_test)
from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(pred,y_test))
print('\n')
print(classification_report(pred,y_test))
#Predict
df2 = pd.read_csv('test.csv')
df2 = df2.drop('Cabin',axis=1)
mean_age = round(df2['Age'].mean())
df2['Age'].fillna(mean_age,inplace=True)
df2['Embarked'].value_counts()
df2['Embarked'].fillna('S',inplace=True)
dummies_embarked = pd.get_dummies(df2['Embarked'],drop_first=True)
df2 = pd.concat([df2.drop('Embarked',axis=1),dummies_embarked],axis=1)
df2 = df2.drop('Name',axis=1)
male_dummies = pd.get_dummies(df2['Sex'],drop_first=True)
df2 = pd.concat([df2.drop('Sex',axis=1),male_dummies],axis=1)
df2 = df2.drop('Ticket',axis=1)
finally_hah = round(df2['Fare'].mean())
df2['Fare'] = df2['Fare'].fillna(finally_hah)
pred2 = logmodel.predict(df2)
done = pd.DataFrame(pred2)
done.columns = ['Survived']
df3 = df2[['PassengerId']]
df4 = pd.concat([df3,done],axis=1)
print(df4)
