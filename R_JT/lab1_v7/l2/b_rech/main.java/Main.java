
import java.util.Stack;
import java.util.Scanner;
public class Main {
    private static Stack<Character> st;
    private static Scanner in;
    private static void fill_st(char etsymb) {
        int count;
        if(!st.empty()) {
            
            while(st.size() > 0) {
                delete_last();
            }
        }
        System.out.println("Максимальный размер стека:");
        count = in.nextInt();

        in.nextLine();
        while(st.size() <= count-1) {
            char el;
            System.out.println("Требуется указать элемент:");
            el = (in.nextLine().charAt(0));
            if(etsymb != el) {
                st.push(el);
            } else {
                break;
            }
        }
        
    }
    private static String show_st() {
        String str = "Элементы стека (сверху вниз).\n";
        for(int i = st.size()-1; i >= 0; i--) {
            str += (st.size()-i)+"ый элемент стека: "+st.get(i)+"\n";
        }
        
        return str;
    }
    private static String search_el(char val) {
        
        return "Элемент находится в позиции: "+st.search(val);
    }
    private static String delete_last() {
        if(!st.empty()) {
            return "Мы удалили элемент: "+st.pop();
        } else {
            return "Стек пуст.";
        }
    }
    private static String get_last() {
        return "Верхний элемент стека: "+st.peek();
    }
    private static String get_len() {
        
        return "Длина стека: "+st.size();
    }
    public static void main (String[] args) {
        int ch = 0;
        st = new Stack<Character>();
        in = new Scanner(System.in);
        do {
            System.out.println("1. Ввести элементы в стек.\n"+
                "2. Отобразить все элементы стека.\n"+
                "3. Поиск позиции элемента стека.\n"+
                "4. Получить верхний элемент стека.\n"+
                "5. Удалить верхний элемент стека.\n"+
                "6. Узнать длину стека.\n"+
                "0. Выход"
            );
	        ch = in.nextInt();
            switch(ch) {
	            case 1:
	                System.out.println("Задайте символ-ограничитель:");
	                in.nextLine();
	                fill_st((in.nextLine()).charAt(0));
	                break;
	            case 2:
                    System.out.println(show_st());
	                break;
                case 3:
                    System.out.println("Укажите элемент для поиска");
                    in.nextLine();
                    System.out.println(search_el((in.nextLine()).charAt(0)));
                    break;
                case 4:
                    System.out.println(get_last());
                    break;
                case 5:
                    System.out.println(delete_last());
                    break;
                case 6:
                    System.out.println(get_len());
                    break;
	            default:
	                ch = 0;
//	                Runtime.getRuntime().exit(0);
	                break;
	        }
	    } while(ch != 0);
	    
	}
}
/*
    https://stackoverflow.com/questions/13942701/take-a-char-input-from-the-scanner
*/
