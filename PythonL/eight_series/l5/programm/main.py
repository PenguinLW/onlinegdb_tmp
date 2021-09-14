import random;
day_list = ["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"];

def day_to_number(day):
    global day_list;
    i = 0;
    pos = 0;
    for el in day_list:
        if(day == el):
            pos = i;
            break;
        i += 1;
    return pos+1;

while(True if (int(input("1. Загадать день\n0. Завершить работу\n")) == 1) else False):
    dn = random.randint(1,7);
    print("{0:s}: {1:s}\n{2:s}: {3:n}\n".format("Вы загадали день", day_list[dn-1], "Порядковый номер дня", day_list.index(day_list[dn-1])+1));
    print("{0:s}: {1:s}\n{2:s}: {3:n}\n".format("Вы загадали день", day_list[dn-1], "Порядковый номер дня", day_to_number(day_list[dn-1])));


