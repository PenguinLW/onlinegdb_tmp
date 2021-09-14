xy = input("Задайте значения x и y (разделитель - пробел): ").split(" ");
for k in range(0, len(xy)):
    xy[k] = float(xy[k]);
x, y = xy;
a = 1 + abs(y - x) + (pow(y - x, 2) / 2) + ((pow(abs(y - x),3)) / 3);
print("Значение выражения: {0:f}".format(a));