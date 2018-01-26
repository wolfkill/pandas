from pandas import DataFrame,Series
import pandas as pd
import  numpy as np
data=pd.date_range('20180126',periods=6)
df=pd.DataFrame(np.random.rand(6,4),index=data,columns=list('ABCD'))
#create a dataframe by passing a numpy array with a datetime index and labled columns;

df2=pd.DataFrame({
    'A':1,
    'B':pd.Timestamp('20180126'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["test","train","test","train"]),
    'F':'foo'
})
s1=pd.Series([1,2,3,4,5,6],index=pd.date_range('20180126',periods=6))

#Getting
df.get('A')
#slices the row
df[0:3]
#Slices by label
df.loc[data[0]]
df.loc[:,['A','B']]
#Selection by Position
df.iloc[3]
#for getting a value explicitly
#Boolean Indexing
df[df.A>0]
#Setting
#Missing Data
df1=df.reindex(index=data[0:4],columns=list(df.columns)+['E'])
df1.loc[data[0]:data[1],'E']=1
df1.dropna(how='any')
df1.fillna(value=5)
pd.isnull(df1)
#Oprations
df.mean()
df.mean(1)
#Apply
df.apply(np.cumsum)
a=df.apply(lambda x:x.max()-x.min())
#Histogramming直方图，直方图
s=pd.Series(np.random.randint(0,7,size=10))
s.value_counts()
s1 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s1.str.lower()
#Merge
#Concat
df3=DataFrame(np.random.randn(10,4))
#breake it to pieces
pieces=[df3[:3],df3[3:7],df3[7:]]
#Join sql style merges
left = DataFrame({'key' : ['foo','foo'],'lval' : [1,2]})
right = DataFrame({'key' : ['foo','foo'],'rval' :[4,5]})
pd.merge(left,right,on='key')
#Appending
df4=DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
h=df4.iloc[3]
i=df4.append(h,ignore_index=True)
#Grouping
df5 = DataFrame({'A' : ['foo','bar','foo','bar','foo','bar','foo','bar'],
                 'B' : ['one','one','two','three','two','two','one','three'],
                 'C':np.random.randn(8),
                 'D':np.random.randn(8)})

#Reshaping  --Stack   --Pivot Tables --Time Series   --Categoricals
df5.groupby('A').sum()
print(df5.groupby('A').sum())




