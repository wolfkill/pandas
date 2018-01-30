#Python Idioms
#if-then/if-then-else on one column, and assignment to another one or more columns:
import itertools
import  pandas as pd
from pandas import  DataFrame,Series
import  numpy as np
df_mask = pd.DataFrame({'AAA': [True] * 4 , 'BBB': [False] * 4 , 'CCC': [True , False] * 2})


df1=DataFrame({'AAA' : [4,5,6,7],'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
dflow=df1[df1['AAA']<=5]
dfhigh=df1[df1.AAA>5]
#Building Criteria
newseries = df1.loc[(df1['BBB']<25)&(df1['CCC']>=-40),'AAA']
# df1.loc[(df1['BBB']>25)|(df1['CCC']>=75),'AAA']=0.1
aVALUE=43.0
#argsort ??
#Selection
df1[(df1.AAA<=6)&(df1.index.isin([0,2,4]))]
#slicing  loc iloc
#Panels   Extend a panel frame by transposing, adding a new dimension, and transposing back to the original dimensions
rng=pd.date_range('20180129',periods=100,freq='D')
data = np.random.randn(100,4)
cols = ['A','B','C','D']
df1,df2,df3 = pd.DataFrame(data,rng,cols), pd.DataFrame(data,rng,cols), pd.DataFrame(data,rng,cols)
pf=pd.Panel({'df1':df1,'df2':df2,'df3':df3})
#Efficiently and dynamically creating new columns using applymap
#applymap
#MultiIndexing 分层索引
df4=DataFrame({'row' : [0,1,2],
               'One_x' : [1.1,1.1,1.1],
               'One_y' : [1.2,1.2,1.2],
               'Two_x' : [1.11,1.11,1.11],
               'Two_y' :[1.22,1.22,1.22]})
df4=df4.set_index('row')
df4.columns=pd.MultiIndex.from_tuples([tuple(c.split('_')) for c in df4.columns])
#stak()方法 return DataFrame or Series
df4=df4.stack(0).reset_index(1)
# df4.columns = ['Sample','All_x']
#MultiIndex复合索引
coords = [('AAA','one'),('AAA','six'),('BBB','one'),('BBB','two'),('BBB','six')]
index=pd.MultiIndex.from_tuples(coords)
df5=pd.DataFrame([11,22,33,44,55],index,['MyData'])
df5.xs('BBB',level=0,axis=0)
df5.xs('six',level=1,axis=0)
#Slicing a MultiIndex
index1 = list(itertools.product(['Ada','Quinn','Violet'],['Comp','Math','Sci']))
headr = list(itertools.product(['Exams','Labs'],['Ⅰ','Ⅱ']))
idx = pd.MultiIndex.from_tuples(index1,names = ['Student','Course'])
cols = pd.MultiIndex.from_tuples(headr)
data = [[70+x+y+(x*y)%3 for x in range(4)] for y in range(9)]
df6 = pd.DataFrame(data, idx, cols)
All = slice(None)
#MssingData  ffill
print(df6.loc[(All,'Math'),All])