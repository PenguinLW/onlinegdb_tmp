import random;
def fill_random(lis, m = 3, n = 3):
    if(m >= 2):
        for i in range(m):
            ch = random.randint(-100,100);
            lis.append(list(range(ch, ch+3)));
    else:
        for i in range(m):
            for j in range(n):
                lis.append(random.randint(-100,100));
    return lis;
def fill_m(lis, m = 3, n = 3):
    if(m >= 2):
        for i in range(m):
            lis.append([]);
            for j in range(n):
                lis[i].append(int(input("Число введи: ")));
    else:
        for i in range(m):
            for j in range(n):
                lis.append(int(input("Число введи: ")));
    return lis;
def show_m(m, l = 3):
    st = "";
    if(l >= 2):
        for i in range(len(m)):
            for j in range(len(m[i])):
                st += "{0:n}\t".format(m[i][j]);
            st += "\n";
    else:
        for i in range(len(m)):
            st += "{0:}\t".format(m[i]);
        st += "\n";
    return st;
def s_meth_1(lis, b, x):
    
    print(
        "Заданная матрица:\n{0:}\nВектор свободных членов:\n{1:}\nВектор x-значений:\n{2:}\n".format(
            show_m(lis),
            show_m(b, 1),
            show_m(x, 1)
        )
    );
    
    
lis = fill_random([]);
b = fill_random([],1);
x = fill_random([],1);
s_meth_1(lis, b, x);

