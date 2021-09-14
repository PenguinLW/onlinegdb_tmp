def readf(fname="input.txt"):
	f = open(fname, "r+");
	s = f.read();
	if(s.find("\n") != -1):
	    d = s[0:-1].split(" ");
	else:
	    d = s.split(" ");
	f.close();
	return d;
def writef(summ, fname="output.txt"):
	f = open(fname, "w+");
	f.write(str(summ));
	f.close();
def main(d):
    f = open("input.txt", "w+");
    f.write("{0:s} {1:s}".format(d[0], d[1]));
    f.close();
    p = 0;
    for el in readf():
    	p = p + int(el);
    writef(p);
main(input().split(" "));
# main(2, 3);
# main(57, 43);
# main(123456789, 673243342);