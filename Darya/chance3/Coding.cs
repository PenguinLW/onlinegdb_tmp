using System;
using System.Security.Cryptography;
using System.Text;
public class Coding {
    public static byte[] encrypt(string message, RSAParameters publicKey) {
        byte[] tmp;
        using (var rsa = new RSACryptoServiceProvider(2048)) {
            rsa.PersistKeyInCsp = false;
            rsa.ImportParameters(publicKey);
            tmp = rsa.Encrypt(Encoding.Unicode.GetBytes(message), true);
        }
        return tmp;
    }
    public static string decrypt(byte[] c, RSAParameters privateKey) {
        byte[] tmp;
        using (var rsa = new RSACryptoServiceProvider(2048)) {
            rsa.PersistKeyInCsp = false;
            rsa.ImportParameters(privateKey);
            tmp = rsa.Decrypt(c, true);
        }
        return Encoding.Unicode.GetString(tmp);
    }
}