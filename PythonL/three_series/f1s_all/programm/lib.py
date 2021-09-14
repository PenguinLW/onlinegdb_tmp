import math;
def miles_to_foot():
    a = float(input("Задайте значение количества миль: "));
    print("Ваше значение, пересчитанное в футах: {0:.2f}".format(a*5280));
def hour_to_sec():
    h, m, s = input("Задайте значение в чч:мм:сс - ").split(":");
    
    print("Количество секун в заданном значении: {0:n}".format(int(h)*3600+int(m)*60+int(s)));
def calc_circumference():
    #c=math.pi*d;c=math.pi*r**2
    pi = 3.14;
    r = float(input("Укажите радиус окружности: "));
    c = pi*r**2;
    
    #print(math.floor(math.pi));
    print("Длина окружности с заданным радиусом - {0:.2f}".format(c));
def calc_deposit():
    deposit = float(input("Укажите сумму вклада: "));
    yer, perc = input("Укажите, как долго планируете хранить свои "+
        "средства лет и годовой процент по вкладу (разделитель - пробел): "
        ).split(" ");
    yer = int(yer);
    perc = float(perc);
    summ = deposit;
    for i in range(0,yer):
        summ += (summ / 100) * perc;
    print("Сумма, которая будет на счёте через {0:n} лет ".format(yer)+
        "при годовом проценте {0:.2f} равна {1:.2f}".format(perc,summ));
def concat_string():
    fs = "Я";
    ss = "изучаю";
    ts = "Python";
    print(fs+" "+ss+" "+ts);
    print("{0:s} {1:s} {2:s}".format(fs,ss,ts));
def calc_age():
    print("Вам {0:s} лет.".format(input("Сколько Вам лет? ")));
def calc_dbp():
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
def get_hundreds():
    numb = int(input("Ваше четырёхзначное число: "));
    print("Цифра, в записи данного числа соответствующая сотням: {0:n}".format(((numb % 1000) // 100)));
    print("Цифра, в записи данного числа соответствующая сотням: {0:s}".format(str(numb)[1]));