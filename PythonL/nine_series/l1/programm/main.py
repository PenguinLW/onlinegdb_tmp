k = 0;
questions = [
    "Сегодня прекрасный день?",
    "Ужасно сегодня спалось?",
    "Вы готовы к приключениям?",
    "Идёмте, тут за углом?",
    "Большинство котов пушисты?",
    "Большинство акул беззубы?",
    "Староста - Ваш друг и советчик?",
    "Тёмное не заметить на белом, так как гармонирует?",
    "Вы сегодня прекрасно выглядите?",
    "Это высокоинтелектуальный опрос?",
    "Это социалогический опрос??",
    "В вопросах есть грамматические ошибки?",
    "Вы довольны?",
    "Вы умны?",
    "Вы счастливы?"
    ];
answers = [
    True,
    False,
    True,
    False,
    True,
    False,
    True,
    False,
    True,
    False,
    True,
    False,
    True,
    False,
    True
    ];
user_answers = [];
def print_question():
    for q in range(len(questions)):
        print("Вопрос №{0:n}\n{1:s}".format(q+1,questions[q]));
        user_answers.append(True if (int(input("1. Да\n2. Нет\n"))) == 1 else False);
        check_answer();
def check_answer():
    global k;
    l = len(user_answers)-1;
    if(user_answers[l] == answers[l]):
        print("Верно");
        k += 1;
    else:
        print("Не верно");
def print_report():
    print("Вы набрали {0:n} баллов из {1:n}".format(k,len(answers)));
    for i in range(len(questions) if len(answers) == len(user_answers) else 0):
        print("Вопрос: {0:s}.\nПравильный ответ: {1:b} - Ваш ответ: {2:b}".format(questions[i], answers[i], user_answers[i]));
def new_game():
    global user_answers, k;
    while(True):
        print_question();
        print_report();
        if(True if (int(input("Желаете попробовать ещё раз?\n1. Да\n2. Нет\n"))) == 1 else False):
            user_answers = [];
            k = 0;
            print("Благодарим за Ваши ответы!");
            pass;
        else:
            user_answers = [];
            k = 0;
            print("Благодарим за Ваши ответы! Всего доброго!");
            break;
new_game();