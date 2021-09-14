name = "Лабораторная работа 3.xlsx";
file = open(name, "r+");
stroka = "";
datetime = "12.03.2019 ";

for st in file:
    if(st[0:11] == datetime):
        stroka += st;
    elif(st.split("\t")[0] != " "):
        stroka += datetime + st;
file.close();
file = open(name, "w+");
file.write(stroka);
file.close();