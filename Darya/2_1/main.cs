using System;
class Programm {
  static void Main() {
      int ch;
      bool flag = true;
      int[] m = new int[0];
      Receiver alice;
      Sender bob;
      
      int number;
      string family;
      
      Console.Write("Введите порядковый номер: ");
      number = Convert.ToInt32(Console.ReadLine());
      Console.Write("Введите фамилию: ");
      family = Console.ReadLine();
      alice = new Receiver(number, family);
      bob = new Sender(alice.getKeys());
      while(flag) {
          Console.WriteLine("1. Боб создаёт сообщение.\n2. Алиса читает сообщение.\n0. Не выход.");
          ch = Convert.ToInt32(Console.ReadLine());
          switch(ch) {
              case 1:
                m = bob.send(Console.ReadLine());
                Console.WriteLine("Посылается зашифрованное сообщение:");
                foreach(int el in m) {
                    Console.Write($"{el} ");
                    
                }
                Console.WriteLine();
                break;
              case 2:
                Console.WriteLine("Получено сообщение:");
                Console.WriteLine(alice.read(m));
                // m = new int[0];
                break;
              case 0:
              default:
                flag = false;
                break;
          }
      }
  }
}