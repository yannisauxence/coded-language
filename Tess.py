import pandas as pd
tx =""
f = pd.read_excel('Records.xlsx', usecols="A:K")
'''print(f)
for x in f:
        tx += x
print(tx)'''
'''print (f.index)'''
print (f.row)
print(len(f.columns))
d = len(f.columns)
z = 0

for x in f.index:
        for y in f.columns.values:
                print (f.at[x,y]," ")
        print("a")
                        
                   
                        

        
