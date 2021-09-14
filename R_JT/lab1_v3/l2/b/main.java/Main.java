
import java.util.Stack;
import java.util.Scanner;
public class Main {
    private static Stack<Integer> st;
    private static Scanner in;
    private static void fill_st(int count) {
        if(!st.empty()) {
            
            while(st.size() > 0) {
                delete_last();
            }
        }
        for(int i = 0; i <= count-1; i++) {
            System.out.println("Требуется указать элемент:");
            st.push(in.nextInt());
        }
        
    }
    private static String show_st() {
        String str = "Элементы стека (сверху вниз).\n";
        for(int i = st.size()-1; i >= 0; i--) {
            str += (st.size()-i)+"ый элемент стека: "+st.get(i)+"\n";
        }
        
        return str;
    }
    private static String search_el(int val) {
        
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
	public static void main(String[] args) {
	    int ch;
	    st = new Stack<Integer>();
	    in = new Scanner(System.in);
	    do {
	        System.out.println("1. Ввести элементы в стек.\n2. Отобразить все элементы стека.\n3. Поиск позиции элемента стека.\n4. Получить верхний элемент стека.\n5. Удалить верхний элемент стека.\n6. Узнать длину стека.\n0. Выход");
	        ch = in.nextInt();
	        switch(ch) {
	            case 1:
	                System.out.println("Максимальный размер стека:");
	                fill_st(in.nextInt());
	                break;
                case 2:
                    System.out.println(show_st());
                    break;
                case 3:
                    System.out.println("Укажите элемент для поиска");
                    System.out.println(search_el(in.nextInt()));
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