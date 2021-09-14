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