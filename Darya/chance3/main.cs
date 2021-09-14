using System;
class Programm {
  static void Main() {
      int ch;
      bool flag = true;
      string m = "";
      Receiver alice = new Receiver();
      Sender bob = new Sender(alice.getKeys());
      while(flag) {
          Console.WriteLine("1. Боб создаёт сообщение.\n2. Алиса читает сообщение.\n0. Не выход.");
          ch = Convert.ToInt32(Console.ReadLine());
          switch(ch) {
              case 1:
                m = bob.send(Console.ReadLine());
                Console.WriteLine("Посылается зашифрованное сообщение:");
                Console.WriteLine(m);
                break;
              case 2:
                Console.WriteLine("Получено сообщение:");
                Console.WriteLine(alice.read(m));
                m = "";
                break;
              case 0:
              default:
                flag = false;
                break;
          }
      }
  }
}