#
iimport numpy as np
import pandas as pd
import random
s=[0,1,2]
apos=list((i,j) for i in s for j in s)
df = pd.DataFrame([[(i, j) for j in s] for i in s])
print(df)
pOX='X'
cOX='O'


def check() :
    for i in range(3) :
        if df[i].nunique()==1:return False,df.iloc[0, i]

        if df.iloc[i].nunique()==1:return False,df.iloc[i,0]

    if pd.Series(np.diag(df)).nunique()==1: return False,pd.Series(np.diag(df))[0]


    if pd.Series(np.diag(np.fliplr(df))).nunique()==1:return False,pd.Series(np.diag(np.fliplr(df)))[ 0]
    if len(apos)==1 :
        print('Draw')
        sys.exit()
    return True,df.iloc[1,1]
cont=True

winOX=''
i=0
for i in range(9):
    if i%2==0:
       p=1
       while p:
          r, c=map(int, input().split())
          if (r, c) in apos: p=0
          else: print('try a valid position')
       df.iloc[r, c]=pOX
       apos.remove((r, c))
       i+=1
    else:
       r,c=random.choice(apos)
       df.iloc[r, c]=cOX
       apos.remove((r, c))
       i+=1
    print(f"{apos} \n{ df}")
    (cont,winOX) =check()

    if not cont:
       print(f"{winOX} won")
       break
