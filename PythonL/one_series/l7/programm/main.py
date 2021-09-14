import math;
xyz1 = input("Координаты x, y, z первой точки (разделитель - пробел): ").split(" ");
xyz2 = input("Координаты x, y, z второй точки (разделитель - пробел): ").split(" ");
for i in range(0, len(xyz1)):
    xyz1[i] = float(xyz1[i]);
for i in range(0, len(xyz2)):
    xyz2[i] = float(xyz2[i]);

print("Расстояние между точками равно {0:f}".format(
            pow(pow((xyz2[0]-xyz1[0]),2)+pow((xyz2[1]-xyz1[1]),2)+pow((xyz2[2]-xyz1[2]),2), 1/2)
        )
    );
x2, x1, y2, y1, z2, z1 = xyz2[0], xyz1[0], xyz2[1], xyz1[1], xyz2[2], xyz1[2];
print("Расстояние между точками равно {0:f}".format(
            pow(pow((x2-x1),2)+pow((y2-y1),2)+pow((z2-z1),2),1/2)
        )
    );

#списочное присваивание
l = len(xyz1) if(len(xyz1) == len(xyz2)) else 0;
list_coords = [];
for i in range(0, l):
    list_coords.append(xyz2[i]);
    list_coords.append(xyz1[i]);
x2, x1, y2, y1, z2, z1 = list_coords;
print("Расстояние между точками равно {0:f}".format(
            pow(pow((x2-x1),2)+pow((y2-y1),2)+pow((z2-z1),2), 1/2)
        )
    );