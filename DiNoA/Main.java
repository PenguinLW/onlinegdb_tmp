import java.util.Arrays;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc;
        Coefficients сoefficients;
        sc = new Scanner(System.in);
//        System.out.println("Коэффициенты уравнения (a, b, c):");
//        сoefficients = new Coefficients(sc.nextDouble(), sc.nextDouble(), sc.nextDouble());
        сoefficients = new Coefficients();
        
        System.out.println("Коэффициенты уравнения:");
        System.out.print("a = ");
        сoefficients.setA(sc.nextDouble());
        System.out.print("b = ");
        сoefficients.setB(sc.nextDouble());
        System.out.print("c = ");
        сoefficients.setC(sc.nextDouble());
        
        System.out.println("Дискриминант: "+ сoefficients.discrim());
        
        System.out.println("Корни уравнения:");
        System.out.println(Arrays.toString(сoefficients.solution()));
    }
}