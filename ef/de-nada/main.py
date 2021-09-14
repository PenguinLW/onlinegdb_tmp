hld = list(range(1, 30+1));
rhld = [el for el in hld if str(el).find("2") != -1];
print(rhld);
print("{0:d} / {1:d}".format(len(rhld), len(hld)));