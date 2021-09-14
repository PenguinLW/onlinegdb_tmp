import random;
secret_number = 0;
def input_guess(guess):
    new_game();
    print("Вы назвали число - {0:n}\nЗагаданное число - {1:n}".format(guess,secret_number));
    if(secret_number == guess):
        print("{0:s}".format("Угадал!"));
    if(secret_number > guess):
        print("{0:s}".format("Меньше! (("));
    if(secret_number < guess):
        print("{0:s}".format("Больше! (("));
def new_game():
    global secret_number;
    secret_number = random.randint(0,100);

input_guess(random.randint(0,100));