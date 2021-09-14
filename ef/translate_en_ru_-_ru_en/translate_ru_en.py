'''
def sort_list(ru,en):
    elmax = ord(ru[0]);
    for i in range(0,len(en)):
        for j in range(0,len(en)):
            if(ord(ru[j]) < elmax):
                ch = ru[j];
                ru[j] = ru[j-1];
                ru[j-1] = ch;
                elmax = ord(ru[j]);
    print("RU - ",ru);
    #return ru,en;
'''
def find_sdvig(ch):
    ru_list = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"];
    en_list = ["f",",","d","u","l","t","`",";","p","b","q","r","k","v","y","j","g","h","c","n","e","a","[","w","x","i","o","]","s","m","'",".","z"];
    #print(len(ru_list)==len(en_list));
    #sort_list(ru_list,en_list);
    sdcode = 0;
    l = 0;
    if(len(ru_list)==len(en_list)):
        l = len(en_list);
    for i in range(0,l):
        if(ru_list[i] == ch):
            sdcode = ord(ru_list[i])-ord(en_list[i]);
        #print("TYT - ",en_list[i],ord(ru_list[i])-ord(en_list[i]));
        #en_code.append(ord(ru_list[i])-ord(en_list[i]));
    return sdcode;
def get_untrtext():
    untr = open("untr.txt","r+");
    str = "";
    for el in untr:
        str += el;
    #print((str.upper()));
    untr.close();
    return str;
def tr_of_en(str):
    tr = open("tr.txt","w+");
    #1025,1072-1103#97-122
    '''
    ord("P");80
    ord("p");112
    ord("З");1047
    ord("з");1079
    '''
    #en_code = find_sdvig([]);
    #print(en_code);
    '''
    #j = 97;
    #while(j < 122)
    for k in range(0,len(str)):
        #sdvig = en_code[k];#967 for p,P,з,З
        j = 97;
        u=0;
        while(j < 122):
            sdvig = en_code[u];
            if(ord(str[k]) == ord(chr(j+sdvig))):
                print(j,sdvig,chr(j+sdvig));
                #print(ord(str[k]), ord(chr(j+sdvig)));
                #print(str[k],en_code[k],sdvig,j,chr(j));
                tr.write(chr(j));
                u += 1;
                #print("{0:10s} - {1:10d} - {2:10s} - {3:10d}\n".format( str[k],ord(str[k]),chr(j),ord(chr(j)) ));
            #if(ord(str[k].upper()) == ord(chr(j-32+967))):
            #    print(j-32,chr(j-32));
            #    print("{0:10s} - {1:10d} - {2:10s} - {3:10d}\n".format( chr(ord(str[k])-32),ord(str[k])-32,chr(j-32),ord(chr(j-32)) ));
            j += 1;
    '''
    for k in range(0,len(str)):
        j = ord(str[k])-find_sdvig(str[k]);
        #print(str[k]," - ",chr(j));
        tr.write(chr(j));
    
        
    #for i in range(0,len(str)):
    #    print("{0:10s} - {1:10d} - {2:10s} - {3:10d}".format(str[i],ord(str[i]),chr(ord(str[i])+50),ord(str[i])+50));
        '''
        if(ord(str[i]) > 50):
            if(ord(chr(ord(str[i])-32)) >= 1040):
                print("{0:10s} - {1:10d} - {2:10s} - {3:10d}".format(str[i],ord(str[i]),chr(ord(str[i])-32),ord(str[i])-32));
                if(ord(str[i]) == 1105):
                    tr.write(chr(1025));
                else:
                    tr.write(chr(ord(str[i])-32));
            else:
                tr.write(str[i]);
        else:
            tr.write(str[i]);
        '''
    tr.close();
tr_of_en(get_untrtext());
"""
    https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
    http://www.cyberforum.ru/python/thread1032244.html
    http://jquery.page2page.ru/index.php5/%D0%9A%D0%BE%D0%B4%D1%8B_%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%BE%D0%B2_%D0%B8_%D0%BA%D0%BB%D0%B0%D0%B2%D0%B8%D1%88
    
"""
