import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression as lr
from sklearn import metrics as mtr
import matplotlib.pyplot as plt

def predexam(tst1,tst2):
    predexam = w1*tst1+w2*tst2+b
    return predexam

data = pd.read_csv('nour1.csv')
inputs, targets = data[['tst1','tst2']], data['exam/60']
model = lr().fit(inputs, targets)
prediction = model.predict(inputs)
loss = mtr.mean_squared_error(targets ,prediction)
"""model.coef_ return two values of coefficient
and model.intercept_ return one value of intercept"""
w1=model.coef_[0]
w2=model.coef_[1]
b =model.intercept_

# show of predexam function
plt.scatter(data['tst1'],data['exam/60'],color='red',label='tst1')
plt.scatter(data['tst2'],data['exam/60'],color='blue',label='tst2')

tst1= np.linspace(0,22,100)
tst2= np.linspace(0,22,100)
y  = w1*tst1+w2*tst2+b
plt.plot(tst1,y,color='green',label='predict exam by tests')

plt.legend()
plt.xlabel('tst')
plt.ylabel('exam')
plt.show()

###################################################################
'''GET NEW DATA'''
exdata = pd.read_csv('exampl.csv')
'''FIND OUT EACH INDEX AND THE LEVEL IT BELONGS TO'''
level1=[]
level2=[]
level3=[]
for index in range(exdata.shape[0]):
    tst1 = exdata[['tst1','tst2'][0]][index]
    tst2 = exdata[['tst1','tst2'][1]][index]
    """PREDICT THE EXAM GRADE FOR EACH INDEX"""
    exam = predexam(tst1,tst2)
    '''DIVIDE THE GRADES INTO TREE SECTION'''
    if 0<exam<8 :
        level1.append(index)
    elif 8<exam<13 :
        level2.append(index)
    elif 13<exam<17 :
        level3.append(index)
        
'''KNOW THE LIST OF NAMES OF EACH LEVEL'''
hls=[] #hight level support
mls=[] #mideum level support
lls=[] #low level support
for i in range(len(level1)):
    name=exdata[['name'][0]][level1[i]]
    hls.append(name)
for k in range(len(level2)):
    name=exdata[['name'][0]][level2[k]]
    mls.append(name)
for j in range(len(level3)):
    name=exdata[['name'][0]][level3[j]]
    lls.append(name)

"""CLASSIFICATION AND SAVING OF DATA ACCORDING TO THE LEVEL OF SUPPORT"""
support = pd.read_csv('support.csv')
for i in range(max(len(hls),len(mls),len(lls))):
    try:
        support[['hight level support','mideum level support','low level support'][0]][i] = hls[i]
    except:
        support[['hight level support','mideum level support','low level support'][0]][i] = ''
for i in range(max(len(hls),len(mls),len(lls))):
    try:
        support[['hight level support','mideum level support','low level support'][1]][i] = mls[i]
    except:
        support[['hight level support','mideum level support','low level support'][1]][i] = ''
for i in range(max(len(hls),len(mls),len(lls))):
    try:
        support[['hight level support','mideum level support','low level support'][2]][i] = lls[i]
    except:
        support[['hight level support','mideum level support','low level support'][2]][i] = ''
support = support.dropna()
print(support)
support.to_csv('support.csv',index=False)

"""HERE I CAN SEE EACH LEVEL AND THE SIZE OF THE STUDENTS"""
h=format((len(level1)/(len(level1)+len(level2)+len(level3)))*100,'.2f')
m=format((len(level2)/(len(level1)+len(level2)+len(level3)))*100,'.2f')
l=format((len(level3)/(len(level1)+len(level2)+len(level3)))*100,'.2f')
sub = [f'{h}% hight level support',f'{m}% mideum level support',f'{l}% low level support']
mark = [h,m,l]
c=['red',(1,1,0),'green']

plt.pie(mark,labels=sub,colors=c)
plt.legend()
plt.show()

    
    
    


