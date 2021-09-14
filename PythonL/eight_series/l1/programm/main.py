lis = [];
flag = False;
ch = 1;
lis.append(ch+1);
while(len(lis) < 6):
    ch += 1;
    for el in lis:
        if((ch % el) != 0):
            flag = True;
        else:
            flag = False;
            break;
    if(flag):
        lis.append(ch);
"""
for x in range(1,15):
    print(x);
    for j in range(1,x):
        if((x % j) != 0):
            flag = True;
        elif((x % j) == 0):
            flag = False;
            break;
    if(flag):
        lis.append(x);
"""
s = "";
for i in range(1,len(lis),2):
    s += "{0:n}\t".format(lis[i]);
print(s);
