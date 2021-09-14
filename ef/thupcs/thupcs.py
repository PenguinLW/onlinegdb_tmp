def get_lowc_text():
    lowcf = open("lowcf.txt","r+");
    str = "";
    for el in lowcf:
        str += el;
    #print((str.upper()));
    lowcf.close();
    return str;
def wif_upc(str):
    uppcf = open("uppcf.txt","w+");
    for i in range(0,len(str)):
        #uppcf.write(str(int(str[i])+100));
        if(ord(str[i]) > 50):
            #print(ord(chr(ord(str[i])-32))+32 == ord(str[i]));
            #if(ord(chr(ord(str[i])-32))+32 == ord(str[i])):
            if(ord(chr(ord(str[i])-32)) >= 1040):
                #print("{0:10s} - {1:10d} - {2:10s} - {3:10d}".format(str[i],ord(str[i]),chr(ord(str[i])-32),ord(str[i])-32));
                if(ord(str[i]) == 1105):
                    uppcf.write(chr(1025));
                else:
                    uppcf.write(chr(ord(str[i])-32));
            else:
                uppcf.write(str[i]);
        else:
            uppcf.write(str[i]);
    uppcf.close();
wif_upc(get_lowc_text());
"""
    https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
    http://www.cyberforum.ru/python/thread1032244.html
"""
