using System;
class HelloWorld {
  static void Main() {
      int t;
      double x, y, a, b;
      //double pi = 3.14;//?Math.PI
      Console.WriteLine("Введите числа:");
      t = Convert.ToInt32(Console.ReadLine());//-6
      x = Convert.ToDouble(Console.ReadLine());//2.7
      
      a = Math.Abs(x);
      b = Math.Sqrt(Math.Pow(x, 2) + Math.Pow(t, 2));
      
      y = Math.Pow(Math.Abs(a-b*x), 1.0/5.0);
      
      Console.WriteLine(y);
  }
}