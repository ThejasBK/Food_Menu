import pandas as pd
import numpy as np

#Selecting only random food from list until now
def menu(df):
    x=np.random.randint(df[0].size)
    print(df[0,x])

#To add new food into file
#Compares if food exists and then adds it
def food(df):
    newFood=input('Please enter the food ')
    for i in df[0]:
        if i.upper()==newFood.upper():
            print('Food exists')
            return
    file=open('food.csv','a')
    file.write(newFood+'\n')
    file.close()
    print('Successufully Entered')
        

n=int(input('Press 1 to show menu or 2 to add a food item '))
df=np.array(pd.read_csv('food.csv'))
df=df.reshape(1,df.size)          #Converting to print result directly
if n==1:
    menu(df)
else:
    food(df)

