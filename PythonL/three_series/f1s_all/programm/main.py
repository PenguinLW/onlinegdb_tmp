import lib;
ch = True;
while(ch != 0):
    ch = int(input("1. Task 1\n2. Task 2\n3. Task 3\n4. Task 4\n5. Task 5\n6. Task 6\n7. Task 7\n8. Task 8\n0. Exit\n"));
    if(ch == 1):
        lib.miles_to_foot();
    elif(ch == 2):
        lib.hour_to_sec();
    elif(ch == 3):
        lib.calc_circumference();
    elif(ch == 4):
        lib.calc_deposit();
    elif(ch == 5):
        lib.concat_string();
    elif(ch == 6):
        lib.calc_age();
    elif(ch == 7):
        lib.calc_dbp();
    elif(ch == 8):
        lib.get_hundreds();