import random;
import math as mt;
secret_number = 0;
flag = False;
def input_guess(guess):
    global flag;
    print("Вы назвали число - {0:n}\nЗагаданное число - {1:n}".format(guess,secret_number));
    if(secret_number == guess):
        print("{0:s}".format("Угадал!"));
        flag = True;
    if(secret_number > guess):
        print("{0:s}".format("Меньше! (("));
    if(secret_number < guess):
        print("{0:s}".format("Больше! (("));

def new_game():
    global secret_number, m, n;
    secret_number = random.randint(m,n);

def start_session():
    global flag, m, n;
    m, n = input("Укажите диапазон загадывания чисел (разделитель - \";\" + \" \"): ").split("; ");
    m = int(m);
    n = int(n);
    new_game();
    count = mt.ceil(mt.log(n-m,2));
    print("Общее количество попыток: {0:n}".format(count));
    while(count > 0):
        guess = random.randint(m,n);
        input_guess(guess);
        count -= 1;
        if(count >= 1):
            print("У Вас осталось {0:n} попыток.".format(count));
            if(True if(int(input("Желаете продолжить?\n1. Да\n2. Нет\n")) == 1) else False):
                if(flag):
                    print("Вы выиграли, но мы рады что не уходите!");
                    flag = False;
            else:
                break;
    if(True if(int(input("Попытки исчерпаны. Желаете сыграть ещё раз?\n1. Да\n2. Нет\n")) == 1) else False):
        start_session();
start_session();

"""
https://planetcalc.ru/4206/
ограничение попыток
у вас осталось столько-то попыток

задание диапазона загадывания числа
предложение продолжить игру
"""