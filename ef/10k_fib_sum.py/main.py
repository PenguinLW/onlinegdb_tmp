tmp_nmb = 0;
current_nmb = 1;
summ = 0;
tmp_str = "{0:n} {1:n} ".format(tmp_nmb, current_nmb);
while(current_nmb < 10000):
    if(current_nmb % 2 != 0):
        summ += current_nmb;
    current_nmb += tmp_nmb;
    tmp_nmb = current_nmb - tmp_nmb;
    if(current_nmb < 10000):
        tmp_str += "{0:n} ".format(current_nmb);
tmp_str += "\n{0:n}".format(summ);
print(tmp_str);
