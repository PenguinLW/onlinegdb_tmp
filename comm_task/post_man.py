import math;
def oount_path(lis):
    if lis > 1:
        lis *= count_path(lis - 1);
    return lis;
point_begin = "Почтовое отделение";
point_location = {
    "Почтовое отделение": (0, 2),
    "Ул. Грибоедова, 104/25": (2, 5),
    "Ул. Бейкер стрит, 221б": (5, 2),
    "Ул. Большая Садовая, 302-бис": (6, 6),
    "Вечнозелёная Аллея, 742": (8, 3),
    "Рыжая Аллея, 2": (4, 3)
};
# for point in point_location:
#     print(
#         "{0:s} - {1:}".format(
#             point,
#             point_location[point]
#         )
#     );
# print(
# #     oount_path(len(point_location) - 1)
#     "Всех возможных маршрутов: {0:}".format(math.factorial(len(point_location) - 1))
# );
def check_dist(dist):
    flag = False;
    for dtmp in distantion:
        if(dist == dtmp[1]):
            flag = True;
    return flag;
def check_name(name):
    flag = False;
    for dname in distantion:
#         print(dname[0][0]);
        if(name == dname[0][0]):
            flag = True;
    return flag;
# def save_dist(names, dist):
#     flag = True;
#     for dtmp in distantion:
#         if(dist == dtmp[1]):
#             flag = False;
#     if(flag):
#         distantion.append([names, dist]);
def count_dist(x1, y1, x2, y2):
    dtmp = math.sqrt(
        math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)
    );
    return dtmp;
distantion = [];
point = point_begin;
while True:
# for point in point_location:
    x1 = point_location[point][0];
    y1 = point_location[point][1];
    name = "";
    dist = [];
    dist_names = [];
    for tmp in point_location:
        x2 = point_location[tmp][0];
        y2 = point_location[tmp][1];
        dtmp = count_dist(
            x1, y1, x2, y2
        );
        if(dtmp > 0):
            name = "From {0:} ({2:}, {3:}) to {1:} ({4:}, {5:}) - ".format(
                point, tmp, x1, y1, x2, y2
            );
            if(not check_name(tmp)):#(not check_dist(dtmp)):
                dist.append(dtmp);
                dist_names.append([point, (x1, y1), tmp, (x2, y2)]);
#                 print(dist, dist_names);
#             print("{0:}{1:}".format(
#                 name,
#                 dtmp
#             ));
#         else:
#             print(tmp);
#     print("");
    
    if(len(distantion) == len(point_location) - 1):
        point = distantion[len(distantion) - 1][0][2];
        tmp = point_begin;
        distantion.append([
            [point, point_location[point], tmp, point_location[tmp]],
            count_dist(
                point_location[point][0], point_location[point][1],
                point_location[tmp][0], point_location[tmp][1]
            )
        ]);
        break;
    else:
        distantion.append([
            dist_names[dist.index(min(dist))],
            min(dist)
        ]);
        point = dist_names[dist.index(min(dist))][2];
#         print(dist);
#         print(distantion);
#         print(dist_names[dist.index(min(dist))]);
#         print(distantion[len(distantion) - 1]);

print("Дорожная карта смены (почта, минимальный маршрут):");
for d in distantion:
    print("From {0:} ({2:}, {3:}) to {1:} ({4:}, {5:}) - {6:}".format(
        d[0][0], d[0][2],#point, tmp
        d[0][1][0], d[0][1][1],#x1, y1
        d[0][3][0], d[0][3][1],#x2, y2
        d[1]#dist
    ));
all_dist = 0;
for d in distantion:
    all_dist += d[1];
print("Расстояние всего маршрута - {0:}".format(all_dist));
