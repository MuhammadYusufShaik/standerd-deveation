import pandas as pd
import statistics as st 
df=pd.read_csv('C:/Users/khada/Downloads/python/c109/height-weight.csv')
height=df['Height(Inches)'].tolist()
mean=st.mean(height)
std=st.stdev(height)
startingpoint=mean-3*std
endingpoint=mean+3*std
firstlist=[]
for h in height:
    if h > startingpoint and h < endingpoint:
        firstlist.append(h)
p=len(firstlist)/len(height)
print(p*100) 