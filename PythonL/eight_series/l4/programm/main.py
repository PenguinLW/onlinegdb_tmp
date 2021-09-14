def add_vector(v, w):
    print("Первая пара векторов: {0:}\nВторая пара векторов: {1:}".format(v, w));
    sv = [];
    for m in range(len(v)):
        sv.append([]);
        for el in range(len(v[m])):
            sv[m].append(v[m][el]+w[m][el]);
    return sv;
print(add_vector([list(range(1,3)),list(range(3,5))], [list(range(5,7)),list(range(7,9))]));
