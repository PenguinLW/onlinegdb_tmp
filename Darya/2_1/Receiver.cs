using System;
using static Coding;
public class Receiver {
    public int[] co_value, fcode;
    private int[] ch_value;
    private int[] snum = new int[25] {
        2, 3, 5, 7, 11,
        13, 17, 19, 23, 29,
        31, 37, 41, 43, 47,
        53, 59, 61, 67, 71,
        73, 79, 83, 89, 97
    };
    public Receiver(int number, string family) {
        fcode = getMessageCode(family.ToLower());
        
        co_value = new int[2] {0, 0};//n, e
        ch_value = new int[4] {0, 0, 0, 0};//p, q, f_n, d
        
        ch_value[0] = (snum.Length-1) - (number-1);
        ch_value[1] = getQ(fcode);
        ch_value[2] = (ch_value[0]-1)*(ch_value[1]-1);
        
        co_value[0] = ch_value[0]*ch_value[1];
        co_value[1] = getExponent(ch_value[2]);
        
        ch_value[3] = getDe(co_value[1], ch_value[2]);
        
        
        // foreach(int el in co_value) {
        //     Console.Write($"{el} ");
            
        // }
        // Console.WriteLine();
        // foreach(int el in ch_value) {
        //     Console.Write($"{el} ");
            
        // }
        // Console.WriteLine();
        
    }
    public string read(int[] cm) {
        return Coding.decrypt(cm, ch_value[3], co_value[0]);
    }
    private int getExponent(int p) {
        Random rnd = new Random();
        int res = rnd.Next(10);
        if((res % 2) != 0 && (p % res) != 0) {
            return res;
        } else {
            return getExponent(p);
        }
    }
    
    public int[] getKeys() {
        return co_value;
    }
    public int getQ(int[] num) {
        int q = 0, index = 0;
        for(int i = 0; i <= num.Length-1; i++) {
            q += num[i];
        }
        if(q > 99) {
            q = q % 100;
        }
        
        for(int i = 0; i <= snum.Length-1; i++) {
            if(snum[i] >= q) {
                index = i;
                break;
            }
        }
        if((snum[index] - q) < (q - snum[index-1])) {
            q = snum[index];
        } else {
            
            q = snum[index-1];
        }
        return q;
    }
}