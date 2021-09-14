from datetime import datetime as dt;
def is_leap_year(year):
    flag = False;
    if(((year % 4) == 0) & ((year % 100) != 0)):
        flag = True;
    elif((year % 400) == 0):
        flag = True;
    else:
        flag = False;
    return flag;
def today():
    return dt.today();
def count_day_of_mounth(mounth,cday):
    day = 0;
    for i in range(0,mounth):
        if((i % 2) != 0):
            if(i == 1):
                day += 29 if(cday == 366) else 28;
            elif(i == 7):
                day += 31;
            else:
                day += 30;
        else:
            day += 31;
    return day;