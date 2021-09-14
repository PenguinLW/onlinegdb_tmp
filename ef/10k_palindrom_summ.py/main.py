current_nmb = 0;
summ = 0;
while(current_nmb < 10000):
    tmp_nmb = str(current_nmb)[::-1]
    if(current_nmb == int(tmp_nmb)):
        summ += current_nmb;
    current_nmb += 1;
print(summ);
