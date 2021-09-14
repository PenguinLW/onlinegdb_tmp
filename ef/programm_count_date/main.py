import lib as dt;
date_now = int(str(dt.today()).split(" ")[0].split("-")[0]);#2019-03-20 04:08:55.110728
date_burn = int(input("Укажите Ваш год рождения"));

cday = 0;
cmounth = 0;
o = 0;
for i in range(date_burn,date_now+1):
    lp = 0;o += 1;
    print(i,dt.is_leap_year(i));
    if(dt.is_leap_year(i)):
        cday += 366;
        lp = 366;
    else:
        cday += 365;
        lp = 365;
    if((i + 1) == date_now):
        count_day_now = 0;
        count_mounth_now = int(str(dt.today()).split(" ")[0].split("-")[1]);
        cmounth += count_mounth_now;
        count_day_now += dt.count_day_of_mounth(count_mounth_now,lp);
        cday += count_day_now;#print((cday+lp)-(lp-count_day_now));
        break;
    else:
        cmounth += 12;
print("{0:n}, {1:n}".format(cmounth,cday));
print(o);