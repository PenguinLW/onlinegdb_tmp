name = "command.txt";
file = open(name,"w+");
stroka = "=СЦЕПИТЬ(";
for n in range(3,99):
    stroka += "{0:s}{1:n}{2:s}".format("Лист1!B",n,(";СЦЕПИТЬ(СИМВОЛ(44);СИМВОЛ(10));" if(n != 98) else ")"));
file.write(stroka);
file.close();