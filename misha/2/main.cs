using System;
class HelloWorld {
  static void Main() {
    double x, y;
    
    Console.WriteLine("Введи число:");
    x = Convert.ToDouble(Console.ReadLine());
    
    y = 0;
    
    if(x > 0) {
        y = Math.Pow(Math.Sin(x), 2);
    } else {
        y = 1 - 2 * Math.Sin(Math.Pow(x, 2));
    }
    Console.WriteLine(y);
  }
}