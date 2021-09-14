using System;
using System.Numerics;
public class Coding {
    public static char[] alphabet = new char[33] {
        'а', 'б', 'в', 'г', 'д', 'е',
        'ё', 'ж', 'з', 'и', 'й', 'к',
        'л', 'м', 'н', 'о', 'п', 'р',
        'с', 'т', 'у', 'ф', 'х', 'ц',
        'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
        'э', 'ю', 'я'
    };

    public static int getDe(int e, int f_n) {
        int d = 0;
        while ((d * e) % f_n != 1) {
            d++;
        }
        return d;
    }
    public static int countUpDegree(int num, int p, int n) {

        Object obj = BigInteger.Pow(num, p) % n;
        num = (int)(BigInteger)obj;
        
        return num;
    }

    public static int[] encrypt(string message, int n, int e) {
        int[] tmp = getMessageCode(message);
        for (int i = 0; i <= tmp.Length - 1; i++) {
            if (tmp[i] != 444) {
                tmp[i] = countUpDegree(tmp[i], e, n);
            }
        }
        return tmp;
    }
    public static int[] getMessageCode(string message) {
        int i = 0;
        int[] code = new int[message.Length];
        foreach(char el in message) {
            for(int n = 0; n <= alphabet.Length - 1; n++) {
                if (el == alphabet[n]) {
                    code[i] = n+1;
                    i++;
                    break;
                } else if (el == ' ') {
                    code[i] = 444;
                    i++;
                    break;
                }
            }
        }
        return code;
    }

    public static string decrypt(int[] c, int d, int n) {
        string message = "";
        for (int i = 0; i <= c.Length - 1; i++) {
            if (c[i] != 444) {
                c[i] = countUpDegree(c[i], d, n);
            }
        }
        return message = getCodeMessage(c);
    }
    public static string getCodeMessage(int[] code) {
        string message = "";
        for (int n = 0; n <= code.Length - 1; n++) {
            if (code[n] != 444) {
                message += alphabet[code[n]-1];
                if (n == 0)
                {
                    message = message.ToUpper();
                }
            } else {
                message += " ";
            }
        }
        return message;
    }
}