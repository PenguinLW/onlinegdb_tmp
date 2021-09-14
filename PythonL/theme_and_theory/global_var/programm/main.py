x= 5;
print(x);
def fun1():
    y = x + 1;
    print(y);
fun1();
x= 5;
print(x);
def fun2():
    x = 7;
    print(x);
fun2();
print(x);
#print(y);
x= 5;
print(x);
def fun3():
    global x;
    x = x + 1;
    print(x);
fun3();
print(x);