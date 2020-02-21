#!C:\Users\theja\AppData\Local\Programs\Python\Python37-32\python.exe

print("Content-Type: text/html\n")
print()
import cgi
import cgitb
cgitb.enable()
print('<html><body style="background-color:#e7e7e7">')
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
    k=0
    days[0]=match()
    for i in range(1,7):
        days[i]=match()
        for j in range(3):
            while days[i][j] in days[i-1]:
                k+=1
                if k in days[i]:
                    continue
                days[i][j]=k
                if k==len(lst)-1:
                    k=0
        
      
weekdays=['Mondays','Tuesday','Wednesday','Thurday','Friday','Saturday','Sunday']
if len(lst)<8:
    print('Insufficient food items')
    print('</body>')
else:
    menu()
    print('<center><table border=5><th>Days</th><th>Breakfast</th><th>Lunch</th><th>Dinner</th>')

    for i in range(7):
        print('<tr><td style="font-weight:bold;">'+weekdays[i]+'</td>')
        for j in range(3):
            print('<td>'+lst[days[i][j]]+'</td>')
        print('</tr>')

print('</center></table></html>')

