
public class Main {
    public static void main(String[] args) {
        Exam e1 = new Exam("24.02.2019","304a","по билетам");
        Fexam fe1= new Fexam("25.02.2019","206","по билетам","бакалавр");
        Proving p1 = new Proving("27.02.2019","206","магистр","2");
        System.out.println(e1);
        System.out.println(fe1);
        System.out.println(p1);
    }
}