using System;
using static Coding;
public class Sender {

    public int[] o_key = new int[2];
    public Sender(int[] co_v) {
        o_key = co_v;
    }
    public int[] send(string m) {

        return Coding.encrypt(m.ToLower(), o_key[0], o_key[1]);
    }

    public void toString() {
        foreach (int n in o_key) {
            Console.Write($"{n}\t");
        }
    }
}