a = [5, 3, 1, -1, -3, 5];
b = list(a);
i = 0;
while(i < len(a)):
    print(a[len(a)-1-i]);
    b[i] = a[len(a)-1-i];
    i += 1;
print(a, "\n", b);
