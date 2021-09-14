
using System;
class HelloWorld {
  static void Main() {
    int x,y,z;
    //string s="";
    x=Convert.ToInt32(Console.ReadLine());
    y=Convert.ToInt32(Console.ReadLine());
    z=Convert.ToInt32(Console.ReadLine());
    if(x > 80 || y > 80 || z > 80) {
        Console.WriteLine("+");//s= "+"; 
    } else {
        Console.WriteLine("-");//s = "-"
    }
    //Console.WriteLine(s);

  }
}