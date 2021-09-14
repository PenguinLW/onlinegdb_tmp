public class Coefficients {
    private double a, b, c, d, x1, x2;

    public Coefficients(){}
/*
    public Coefficients(double a, double b, double c){
        this.a = a;
        this.b = b;
        this.c = c;
    }
*/
    public void setA(double a){
        if(a != 0)
            this.a = a;
        else
            System.out.println("Первый коэфициент не может равняться 0");
    }
    public void setB(double b){
        this.b = b;
    }
    public void setC(double c){
        this.c = c;
    }
    public double getA(){
        return a;
    }
    public double getB(){
        return b;
    }
    public double getC(){
        return c;
    }
    public double getD(){
        return c;
    }
    
    public double discrim() {
        return d = Math.sqrt(Math.pow(b,2)-4*a*c);
    }
    public double[] solution() {
        double[] solve;
        if(b != 0 && c != 0) {
            solve = new double[2];
            solve[0] = (-b + Math.sqrt(d)) / (2 * a);
            solve[1] = (+b + Math.sqrt(d)) / (2 * a);
        }
        else if(b != 0 && c == 0) {
            solve = new double[2];
            solve[0] = 0;
            solve[1] = -(b / a);
            
        }
        else if(b == 0 && c != 0) {
            solve = new double[2];
            solve[0] = Math.sqrt(c / a);
            solve[1] = -Math.sqrt(c / a);
            
        }
        else {
            solve = new double[1];
            solve[0] = 0;
            
        }
        return solve;
    }
}