
import java.util.Stack;
import java.util.Scanner;
public class Main {
    private static  Stack<Auto> st;
    private static Scanner in = new Scanner(System.in);
    private static void in_auto() {
        String cnumb, ccolor, cmake, cmodel;
        in.nextLine();
        System.out.print("Номер авто: ");
        cnumb = in.nextLine();
        System.out.print("Цвет авто: ");
        ccolor = in.nextLine();
        System.out.print("Марка авто: ");
        cmake = in.nextLine();
        System.out.print("Модель авто: ");
        cmodel = in.nextLine();
        st.push(new Auto(cnumb, ccolor, cmake, cmodel));
    }
    private static String out_auto(int pos) {
        if(st.size() == 0 || (pos <= 0 || pos > st.size())) {
            return "Авто выбрано неверно, попробуйте ещё раз";
        }
        int n = 0;
        String stroka;
        Stack<Auto> ts;
        
        stroka = "";
        ts = new Stack<Auto>();
        
        Auto au = st.get(pos-1);
        for(int i = st.size()-1; i >= 0; i--) {
            if(!(st.get(st.size()-1-i)).equals(au)) {
                (st.get(i)).setUsed();
                n++;
            } else {
                break;
            }
        }
        for(int i = 1; i <= n; i++) {
            ts.push(st.pop());
        }
        stroka += delete_last();
        
        while(ts.size() > 0) {
            st.push(ts.pop());
        }
        return stroka;
    }
    private static String show_st() {
        String str = "Все авто на стоянке (начнём с ближайшего к выходу).\n";
        for(int i = st.size()-1; i >= 0; i--) {
            str += (st.size()-i)+"е авто: "+(st.get(i)).toString()+"\n";
        }
        return str;
    }
    private static int search_el(Auto val) {
        return st.search(val);
    }
    private static String delete_last() {
        if(!st.empty()) {
            return "\tНас сегодня покинул:\n"+(st.pop()).toString();
        } else {
            return "На стоянке никого.";
        }
    }
    private static String get_last() {
        return "Верхний элемент стека: "+st.peek();
    }
    private static String get_len() {
        return "В нашем парке сейчас: "+st.size();
    }
    public static void main(String[] args) {
        int ch;
        st = new Stack<Auto>();
        in = new Scanner(System.in);
        do {
            System.out.println("1. Хочу на вашу стоянку!!\n2. Пришли забрать свой автомобиль?\n3. Сколько у вас машин?\n0. Всего доброго!!");
            ch = in.nextInt();
            switch(ch) {
                case 1:
                    in_auto();
                    break;
                case 2:
                    System.out.print("Укажите позицию, на которой находится ваше авто: ");
                    System.out.println(out_auto(in.nextInt()));
                    break;
                case 3:
                    System.out.println(get_len());
                    System.out.println(show_st());
                    break;
                default:
                    ch = 0;
//                    Runtime.getRuntime().exit(0);
                    break;
            }
        } while(ch != 0);
    }
}
