tmp_dict = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}
curr_nmb = 10;
tmp_str = "";
count = 0;
while(curr_nmb <= 2660):
    tmp_str += "X";
    
    # if(curr_nmb == 50):
    #     tmp_str = "L";
    # if(curr_nmb == 90):
    #     tmp_str = "XC";
    # if(curr_nmb == 100):
    #     tmp_str = "C";
    
    # if(tmp_str.find("I"*4) != -1):
    #     tmp_str = tmp_str.replace("I"*4, "IV");
    # if(tmp_str.find("I"*5) != -1):
    #     tmp_str = tmp_str.replace("I"*5, "V");
    # if(tmp_str.find("V"+"I"*4) != -1):
    #     tmp_str = tmp_str.replace("V"+"I"*4, "IX");
    
    
    # if(tmp_str.find("C"*4) != -1):
    #     tmp_str = tmp_str.replace("C"*4, "CD");
    # if(tmp_str.find("L"+"X"*4) != -1):
    #     tmp_str = tmp_str.replace("D"+"X"*4, "CM");
    
    
    
    # if(tmp_str.find("X"*4) != -1):
    #     tmp_str = tmp_str.replace("X"*4, "XL");
    # if(tmp_str.find("L"+"X"*4) != -1):
    #     tmp_str = tmp_str.replace("L"+"X"*4, "XC");
    if(curr_nmb < 100):
        # if(curr_nmb % 10 > 0):
        #     if(curr_nmb % 10 < 4):
        #         tmp_str += "I"*(curr_nmb % 10);
        #     elif(curr_nmb % 10 == 4):
        #         tmp_str += "IV";
        #     elif(curr_nmb % 10 == 5):
        #         tmp_str += "V";
        #     elif(curr_nmb % 10 > 5):
        #         if(curr_nmb % 10 < 9):
        #             tmp_str += "V"+"I"*(curr_nmb % 10);
        #         elif(curr_nmb % 10 == 9):
        #             tmp_str += "IX";
        if(curr_nmb % 100 == 40):
            tmp_str = tmp_str.replace("X"*4, "XL");
        if(curr_nmb % 100 == 50):
            tmp_str = "L";
        if(curr_nmb % 100 == 90):
            tmp_str = tmp_str.replace("L"+"X"*4, "XC");
    elif(curr_nmb >= 100):
        if(curr_nmb % 100 == 40):
            tmp_str = tmp_str.replace("X"*4, "XL");
        if(curr_nmb % 100 == 50):
            tmp_str = tmp_str.replace("XL"+"X", "L");
        if(curr_nmb % 100 == 90):
            tmp_str = tmp_str.replace("L"+"X"*4, "XC");
        if(curr_nmb % 100 == 0):
            tmp_str = "C"*((curr_nmb % 1000) // 100);
    if(curr_nmb // 1000 > 0):
        if(curr_nmb % 1000 == 0):
            tmp_str = "M"*(curr_nmb // 1000);
        if(curr_nmb % 1000  >= 100):
            if(curr_nmb % 100  == 0):
                tmp_str = "M"*(curr_nmb // 1000)+tmp_str;
    
    
    if(curr_nmb == 900):
        tmp_str = "CM";
    
    
    if(tmp_str.find("X"*5) != -1):
        tmp_str = tmp_str.replace("X"*5, "L");
    if(tmp_str.find("L"*2) != -1):
        tmp_str = tmp_str.replace("L"*2, "C");
    if(tmp_str.find("C"*5) != -1):
        tmp_str = tmp_str.replace("C"*5, "D");
    if(tmp_str.find("D"*2) != -1):
        tmp_str = tmp_str.replace("D"*2, "M");
    
    for el in tmp_str:
        if(el == "X"):
            count += 1;
    
    print("{0:n} - {1:s}\n".format(curr_nmb, tmp_str));
    curr_nmb += 10;
print(count+260);
