#trying to get the
import pandas as pd

file=open("data2","r")
var=file.readlines()
print(var)
dfs={}
print(type(var))
for i in var:
    temp=i.split()
    temp1=temp[:1]
    temp2=' '.join(temp[1:])
    dfs[temp2] = ""+str(temp1)

print(dfs)
df= pd.Series(dfs).to_frame()
#
print(df)