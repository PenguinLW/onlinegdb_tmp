def lazy_beast(fname):
    st = "";
    
    tmp_f = open(fname, "r+");
    st += ("si = [\n");
    for el in tmp_f:
        if(el.find("\n") != -1):
            el = el[:len(el)-1];
        st += "{0:s}\"{1:s}\",{2:s}".format("\t",el,"\n");
    st = st[:len(st)-2];
    st += ("\n];");
    st += ("\n#print(si);");
    st += """
def find_me(si):
    print(si[si.index("Ковальский Роман Олегович")]);
find_me(si);
    """;
    tmp_f.close();
    
    tmp_f = open("lib.py", "w+");
    for ch in st:
        tmp_f.write(ch);
    tmp_f.close();
    import lib;
    #tmp_f = open("lib.py", "w+");
    #tmp_f.delete();
    #tmp_f.close();
    import os;
    os.remove("lib.py");
#spisok = open("spisok_IGU.xls", "w+");
#print(spisok);
#for el in spisok:
#    print(el);
#spisok.close();
#lazy_beast("");
lazy_beast("listcard_IGU.txt");