using System;
using System.Security.Cryptography;
using System.Text;
using static Coding;
public class Receiver {
    private static RSAParameters publicKey, privateKey;
    public Receiver() {
        using(var rsa = new RSACryptoServiceProvider(2048)) {
            rsa.PersistKeyInCsp = false;
            publicKey = rsa.ExportParameters(false);
            privateKey = rsa.ExportParameters(true);
        }
        
    }
    public string read(string cm) {
        
        return Coding.decrypt(Convert.FromBase64String(cm), privateKey);
    }
    public RSAParameters getKeys() {
        return publicKey;
    }
}