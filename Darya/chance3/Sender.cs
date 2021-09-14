using System;
using System.Security.Cryptography;
using System.Text;
using static Coding;
public class Sender {
    
    public RSAParameters publicKey;
    public Sender(RSAParameters pK) {
        publicKey = pK;
    }
    public string send(string m) {
        
        return Convert.ToBase64String(Coding.encrypt(m, publicKey));
    }
}