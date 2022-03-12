password=input("enter the password:")
a=[]
b=[]
c=[]
d=[]
for i in password:
    if i=="@" or i=="#" or  i=="&":
        a.append(i)
    elif i>="A" and  i<="Z":
        b.append(i)
    elif i>="a" and  i<="z":
        c.append(i)
    elif i>"0" and  i<"9":
        d.append(i)
print(a)
print(b)
print(c)
print(d)
