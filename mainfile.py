import numpy as np
import pandas as pd
from dbman import dbman








df = pd.read_excel (r'missing_data.xlsx')
numlist= []
count = 0;

for row in df['رقم البطاقه']:

    if pd.isna(row) and pd.isna(df['الايميل'][count])  :
       #print(row , '--' , df['الايميل'][count])
       numlist.append(count)

    count+=1

#df = df.drop(numlist)
############
mw = dbman()
count = 0;
for row in df['رقم البطاقه']:
    theemail =False
    thenational_id = False
    if pd.notna(row):
           thenational_id = row
    if pd.notna(df['الايميل'][count]):
           theemail = df['الايميل'][count]
    if theemail or thenational_id:
       if mw.canHaveOne(theemail,thenational_id) == False:
            numlist.append(count)
    else:
        numlist.append(count)
    count += 1
df = df.drop(numlist)

df.to_excel("valid_certified.xlsx", index=False, encoding='utf8')
print(df)