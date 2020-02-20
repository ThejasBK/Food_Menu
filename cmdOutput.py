#This program gives me a command line output

import pandas as pd
import numpy as np
import sys

def match(df):
    y,z=-1,-1
    x=np.random.randint(df.size)
    y=np.random.randint(df.size)
    z=np.random.randint(df.size)
    while y==x:
        y=np.random.randint(df.size)
    while z==x or z==y:
        z=np.random.randint(df.size)
    return [x,y,z]

def additional(days,i):
    return (k for k in [x for x in list(set(range(df[0].size))-set(days[i]))] if k not in days[i-1])

#To display Menu
def menu(df):
    days=dict()
    x=np.random.randint(df[0].size)
    days[0]=match(df[0])
    for i in range(1,7):
        days[i]=[x for x in match(df[0]) if x not in days[i-1]]
        while len(days[i])!=3:
            x=additional(days,i)
            days[i].append(x.__next__())
    week_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for i in range(7):
        print(week_days[i],end=': ')
        for j in days[i]:
            print('"'+df[0,j]+'"',end=' ')
        print()            
  
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

def execute():
     while(True):
        n=int(input('Press 1 to show menu or 2 to add a food item '))
        if n==1:
            menu(df)
            sys.exit()
        elif n==2:
            food(df)
            sys.exit()
        else:
            print('Enter the correct value')
        print('------------------------------')

if __name__=='__main__':
    try:
        print('------------------------------')
        df=np.array(pd.read_csv('food.csv'))
        df=df.reshape(1,df.size)          #Converting to print result directly
        count=df.size
        while count<7:
            print('Required number of food items are not present')
            food(df)
            count+=1
        execute()
    except(FileNotFoundError,IOError):
        print('File not found error')
        sys.exit()
    except(StopIteration):
        df=np.array(pd.read_csv('food.csv'))
        df=df.reshape(1,df.size)          #Converting to print result directly
        days=dict()
        x=np.random.randint(df[0].size)
        days[0]=match(df[0])
        for i in range(1,7):
            days[i]=[x for x in match(df[0]) if x not in days[i-1]]
        while len(days[i])!=3:
            x=additional(days,i)
            days[i].append(x.__next__())
        week_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        for i in range(7):
            print(week_days[i],end=': ')
            for j in days[i]:
                print('"'+df[0,j]+'"',end=' ')
            print()
