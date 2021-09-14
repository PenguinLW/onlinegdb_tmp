def string_list_join(string_list):
    fst = "";
    for el in string_list:
        fst += el;
    
    return fst;
print(string_list_join(list("неправда")));
