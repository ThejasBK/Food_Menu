#!C:\Users\theja\AppData\Local\Programs\Python\Python37-32\python.exe

print("Content-Type: text/html\n")
print()
import cgi
import cgitb
#import pandas as pd
#import numpy as np
cgitb.enable()
print('<html><body bgcolor="black"')
lst=[]
f=open('file.txt','r')
for line in f:
    line=line.rstrip()
    lst.append(line)
    
import random
food_menu=[]
days=dict()
def match():
    y,z=-1,-1
    x=random.randint(0,len(lst)-1)
    y=random.randint(0,len(lst)-1)
    z=random.randint(0,len(lst)-1)
    while y==x:
        y=random.randint(0,len(lst)-1)
    while z==x or z==y:
        z=random.randint(0,len(lst)-1)
    return [x,y,z]

def menu():
    days[0]=match()
    for i in range(1,7):
        days[i]=match()
    for i in range(1,7):
        for j in range(3):
            while days[i][j] in days[i-1]:
                days[i][j]=random.randint(0,len(lst)-1)
    for i in range(1,7):
        d=set(days[i])
        while len(d)!=3:
            d.add(random.randint(0,len(lst)-1))
        #for j in d:
        days[i]=list(d)
weekdays=['Mondays','Tuesday','Wednesday','Thurday','Friday','Saturday','Sunday']
menu()
print('</body><center><table border=5 bgcolor="white"><th>Days</th><th>Breakfast</th><th>Lunch</th><th>Dinner</th>')
for i in range(7):
    print('<tr><td style="font-weight:bold;">'+weekdays[i]+'</td>',end=': ')
    for j in range(3):
        print('<td>'+lst[days[i][j]]+'</td>')
    print('</tr>')

print('</center></table></html>')

