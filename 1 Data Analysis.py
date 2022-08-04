import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


""" We show data in the form of a table in order to understand it"""
data = pd.read_csv('nour school grades.csv')
data=data[['nom&prenom','tst1','tst2','exam/60','moy','coef','moyfin','obser']]
print(data)
print(data.shape)

"""We only need the prediction of the exam through the first and second test data"""
data = data[['tst1','tst2','exam/60']]
print(data)
print(data.shape)

"""When we show this data, we notice that there are missing data and written on it abs"""
data = pd.read_csv('nour school grades.csv',na_values=["abs",np.nan])[['tst1','tst2','exam/60']]
print(data.isnull().sum())

"""You can delete those values"""
data = data.dropna()
print(data)
print(data.shape)

"""We must draw data to know the relationship between each other"""
plt.scatter(data['tst1'],data['exam/60'],color='red',label='tst1')
plt.legend()
plt.xlabel('tst')
plt.ylabel('exam')
plt.show()

"""We must make the exam scores in the same range of first and second test By dividing it on 3"""
data.to_csv('nour1.csv',index=False)
data = pd.read_csv('nour1.csv')

for i in range(data.shape[0]):
    data[['exam/60'][0]][i] = data[['exam/60'][0]][i] / 3   #dividing on 3

print(data)
print(data.shape)

data.to_csv('nour1.csv',index=False)
data = pd.read_csv('nour1.csv')

"""Now we can redraw the data in order to see the relationship"""
plt.scatter(data['tst1'],data['exam/60'],color='red',label='tst1')
plt.scatter(data['tst2'],data['exam/60'],color='blue',label='tst2')
plt.legend()
plt.xlabel('tst')
plt.ylabel('exam')
plt.show()
"""As we notice the first test, in terms of the exam is proportional. As is the case with the second test, in terms of the exam"""
############################################## Now multiple linear regression can be created
