def check_tmp_str(tmp):
    '''
    проверка одной строки (верт/диагон/гориз)
    '''
    if 'X'*5 in tmp:
        print('X - наш проигравший!')
        return True
    if 'O'*5 in tmp:
        print('O - наш проигравший!')
        return True
    return False

def check_right_diag(mapw):
    '''
    собираем из каждой диагонали строку и отдаём каждую на проверку (вдруг кто уже проиграл)
    '''
    i = 0
    j = 0
    while i >= len(mapw) - 1:
        I = i
        results = ''
        while (I >= 0) | (j <= i):
            results += mapw[I][j]
            I -= 1
            j += 1
        i += 1
        j = 0
        if check_tmp_str(results):
            return True
    
    j = 1
    i = len(mapw) - 1
    while j >=  len(mapw) - 1:
        I = i
        J = j
        results = ''
        while I > 0:
            if J <= len(mapw) - 1:
                results += mapw[I][J]
                I -= 1
                J += 1
            else:
                break
        j += 1
        if check_tmp_str(results):
            return True
    
    return False
    
def check_left_diag(mapw):
    '''
    собираем из каждой диагонали строку и отдаём каждую на проверку (вдруг кто уже проиграл)
    '''
    i = 0
    j = 0
    while i <= len(mapw) - 1:
        I = i
        results = ''
        while (I >= 0) | (j <= i):
            results += mapw[I][j]
            I -= 1
            j += 1
        i += 1
        j = 0
        if check_tmp_str(results):
            return True
    
    j = 1
    i = len(mapw) - 1
    while j <=  len(mapw) - 1:
        I = i
        J = j
        results = ''
        while I > 0:
            if J <= len(mapw) - 1:
                results += mapw[I][J]
                I -= 1
                J += 1
            else:
                break
        j += 1
        if check_tmp_str(results):
            return True
    
#     for i in range():
#         for j in range():
#    return True
    return False

def check_vert_row(mapw):
    '''
    собираем из каждой вертикали строку и отдаём каждую на проверку (вдруг кто уже проиграл)
    '''
    i = 0
    for i in range(len(mapw[i])-1):
        results = ''
        for j in range(len(mapw)-1):
            results += mapw[j][i]
        if check_tmp_str(results):
            return True
    return False

def check_hor_row(mapw):
    '''
    собираем из каждой горизонтали строку и отдаём каждую на проверку (вдруг кто уже проиграл)
    '''
    for row in mapw:
        results = ''
        for el in row:
            results += el
        if check_tmp_str(results):
            return True
    return False

def show_mapw(map):
    '''
    здесь превращаем данные игровой сетки (списка) в двумерный список (последующая обработка с ним)
    '''
    new_map = list()
    for i in range(0, len(map), 10):
        new_map.append([])
        for j in range(i, i+10):
            new_map[len(new_map) - 1].append(map[j])
    
    return new_map

def agressive_computer(map, loc, val, nm):
    '''
    компьютер отвечает каким-то ходом (нацеленным на "не проиграть" - не собрать пять в ряд)
    '''
    if loc+1 < nm:
        make_mark(map, loc+1, val, nm)
    elif loc-1 < nm:
        make_mark(map, loc-1, val, nm)
    
    return loc

def make_mark(map, loc, val, nm):
    '''
    ставится отметка в игровую сетку (от любого из участников)
    '''
    if (loc > 0) & (loc <= nm):
        if map[loc - 1] == '.':
            map[loc-1] = val.upper()

def set_map(new_map, nm = 5):
    '''
    подготавливаем игровую сетку для игры
    '''
    for i in range(nm):
        new_map.append('.')
    return new_map;

def show_map(map):
    '''
    здесь смотрим игровую сетку
    '''
    tmp = 0
    results = '\n'
    for i in range(1, len(show_mapw(map))):
        results += '  {0:} '.format(i)
    results += '\n'
    results += '_'*4*10+'\n'
    results += '|'
    for i in range(len(map)):
        results += ' {0:s} |'.format(map[i])
        tmp += 1;
        if tmp == 10:
            results += '{0:}\n|'.format(i+1)
            tmp = 0
    
    results = results[:-1] + '_'*4*10 + '\n'
    
    return results
import random
# задаём размер для квадратной игровой сетки
nm = 100
#инициализируем её
map = set_map(list(), nm)
mark = input('За кого играем (x или o): ')
if 'o' in mark:
    agressive_computer(
        map,
        int(random.randint(1, nm)),
        'x',
        nm
    )
    print('Компьютер выполнил ход. Ваш черёд')
else:
    print('Ход человека первый.')

print(show_map(
    map
))
while True:
    make_mark(
        map,
        agressive_computer(
            map,
            int(input('Куда ставить (номер порядковый): ')),
            'o' if mark.lower() == 'x' else 'x',
            nm
        ),
        mark,
        nm
    )
    print(show_map(
        map
    ))
#     проверка - вдруг кто победил и выход если да
    mapw = show_mapw(map)
    if check_hor_row(mapw) | check_vert_row(mapw) | check_left_diag(mapw) | check_right_diag(mapw):
        break
#mapw = show_mapw(map)
#for el in mapw:
#    print(el)
