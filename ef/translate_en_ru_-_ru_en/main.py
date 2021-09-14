while(True):
    flag = int(input("1. Исправить раскладку en_ru\n2. Исправить раскладку ru_en\n0. Выход\n"));
    if(flag == 1):
        import translate_en_ru;
    elif(flag == 2):
        import translate_ru_en;
    elif(flag == 0):
        print("Всего доброго!");
        break;