#!C:\Users\theja\AppData\Local\Programs\Python\Python37-32\python.exe

print('Content-Type:text/html\n')
print()
import cgi
import cgitb
cgitb.enable()
print('<html>')

lst=[]
flag=0
#Adding element into file
f=open('file.txt','r')
form=cgi.FieldStorage()
for line in f:
    line=line.rstrip()
    lst.append(str(line).upper())
f.close()
f=open('file.txt','a')
f.write(form['foodText'].value+'\n')
f.close()
#Displaying file contents
f=open('file.txt','r')
print('<ul>')
for line in set(f):
    line=line.rstrip()
    print('<li>'+line+'</li>')
print('</ul>')
print('</html>')
