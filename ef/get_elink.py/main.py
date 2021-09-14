def set_elink(link):
    if(link[len(link)-1] == "\n"):
        link = link[0:len(link)-1];
    st = tmp_st = "";
    pos_br = 0;
    ouf = open("ouf.txt", "a+");
    #[https://][p5js_kbase/wiki/theme/1/1/1/theme/]
    #https://p5js_kbase/blob/master/wiki/theme/1/1/1/sketch/sketch.js
    link = link.split("kovalsky95.github.io/");
    st += link[0];
    st += "github.com/Kovalsky95/";
    for i in range(len(link[1])):
        if(link[1][i] != "/"):
            st += link[1][i];
        else:
            pos_br = i;
            break;
    st += "/edit/master/";
    for i in range(pos_br+1, len(link[1])-6):
        st += link[1][i];
    st += "sketch/sketch.js\n";
    ouf.write(st);
    ouf.close();
    return st;
def get_vlink():
    lis = [];
    inf = open("inf.txt", "r+");
    for el in inf:
        lis.append(set_elink(el));
    
    inf.close();
    return lis;
tmp_f = open("ouf.txt", "w+");
tmp_f.close();
get_vlink();