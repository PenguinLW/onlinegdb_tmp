def is_leap_year(year):
    flag = False;
    if(((year % 4) == 0) & ((year % 100) != 0)):
        flag = True;
    elif((year % 400) == 0):
        flag = True;
    else:
        flag = False;
    return flag;
    