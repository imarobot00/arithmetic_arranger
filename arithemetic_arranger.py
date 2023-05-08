import operator

#define operators you wanna use
allowed_operators={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}

list_of_string= ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
a=list()
b=list()
c=list()
for number in range(len(list_of_string)):
    list_of_string[number]=list_of_string[number].split()
    a.append(int(list_of_string[number][0]))
    b.append(int(list_of_string[number][2]))
    c.append(allowed_operators[list_of_string[number][1]](a[number],b[number]))
d=list()
for i in range(len(c)):
    c[i]=str(c[i])
    d.append(len(c[i]))
for i in range(len(c)):
    a[i]=str(a[i])
    print((a[i].rjust(d[i]+1)),end=" ")
print("")
for i in range(len(c)):
    b[i]=str(b[i])   
    print(((list_of_string[i][1]) + b[i]).rjust(d[i]+1), end=" ")
print("")
e=list()
for i in range(len(c)):
    e.append(d[i])
    print((("-")*e[i]).rjust(d[i]+1),end=" ")
print("")
for i in range(len(c)):
    c[i]=str(c[i])   
    print((c[i].rjust(d[i]+1)),end=" ")
        

