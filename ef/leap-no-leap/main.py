import datetime as dt;
def is_leap_year(y=int(str(dt.datetime.today())[:4])):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                print("leap");
            else:
                print("noleap");
        else:
            print("leap");
    else:
        print("noleap");
is_leap_year();
is_leap_year(2020);
is_leap_year(2021);
is_leap_year(2022);
is_leap_year(2023);
is_leap_year(2024);