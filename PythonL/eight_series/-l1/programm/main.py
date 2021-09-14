x = [1, 2, 4];
y = list(x);
y[0] = -125;
print(x);
print(y);
"""
x = [2, 6];
y = x*6;
print(y);
x = range(3, 125, 50);
print(x);
for i in x:
    print(i);

g = [];
for i in range(3, 125, 50):
    g.append(i);
for i in x:
    g.append(i);
print(g);

x = list(range(3, 125, 50));
print(x);
for i in range(4):
    x.append(int(input("Введи: ")));
print(x);
"""
"""
a = [4, 1, 2, 3];
#print(a);
b = [-6, 0.05, "0.05", True, 9];
#print(b);
#Список списков
c = [
    [-3, 12],
    [0, 1],
    [5, 5]
];
#print(c);

print(a[2]);
#print(a[4]);
print(a[-1]);
print(len(a));
print(len(c));
print(len(b));

x = [25, 21, 45];
print(x[-1]);
print(x[-2]);
print(x[-3]);
#print(x[-4]);
print(c[0][1]);

print(b[0:2]);
print(b[2:2]);
#k = [b[1],b[3]];
#print(k);
print(b);
b[2] = 25;
b[1] = [];
print(b);
print(a + b);
"""