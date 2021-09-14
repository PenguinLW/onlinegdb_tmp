
import java.util.Scanner;
import java.util.ArrayList;
import static java.lang.Math.pow;
public class Main {
    private static Scanner in;
    private static ArrayList<Student> list_students;
    private static void sort_list_st() {
        ArrayList<Student> st_min_z, st_av_count;
        int min_z = 7500;
        
        st_min_z = new ArrayList<Student>();
        st_av_count = new ArrayList<Student>();
        for(int i = 0; i <= list_students.size()-1; i++) {
            if((list_students.get(i)).getMany() < (min_z*2)) {
                st_min_z.add(list_students.get(i));
            } else {
                st_av_count.add(list_students.get(i));
            }
        }
        list_students.clear();
        st_min_z = sort_of_avcount(st_min_z);
        st_av_count = sort_of_avcount(st_av_count);
        for(int i = 0; i <= st_min_z.size()-1; i++) {
            list_students.add(st_min_z.get(i));
        }
        for(int i = 0; i <= st_av_count.size()-1; i++) {
            list_students.add(st_av_count.get(i));
        }
    }
    private static ArrayList<Student> sort_of_avcount(ArrayList<Student> list) {
        
        ArrayList<Student> listofs;
        listofs = new ArrayList<Student>();
        while(list.size() > 0) {
            int index = 0;
            for(int i = 1; i <= list.size()-1; i++) {
                if((list.get(i)).getAvCount() > (list.get(index)).getAvCount()) {
                    index = i;
                    
                }
            }
            listofs.add(list.get(index));
            list.remove(index);
        }
        list.clear();
        return listofs;
    }
	public static void main(String[] args) {
	    int ch;
	    in = new Scanner(System.in);
	    list_students = new ArrayList<Student>();
	    
	    do {
	        System.out.println("1. Добавить данные о студенте.\n2. Отобразить список студентов для заселения.\n0. Выход.");
	        ch = in.nextInt();
	        switch(ch) {
	            case 1:
	                String fio, group;
	                double av_count, many;
	                System.out.println("Укажите данные о студенте. После указания каждого значения подтверждайте ввод по клавише Enter.");
	                System.out.println("ФИО:");
	                in.nextLine();
	                fio = in.nextLine();
	                System.out.println("Группа:");
	                group = in.nextLine();
	                System.out.println("Средний балл:");
	                av_count = in.nextDouble();
	                System.out.println("Доход на члена семьи:");
	                many = in.nextDouble();
	                list_students.add(new Student(fio, group, av_count, many));
	                sort_list_st();
	                break;
	            case 2:
	                for(int i = 0; i <= list_students.size()-1; i++) {
	                    System.out.println(list_students.get(i));
	                }
	                break;
	            default:
	                ch = 0;
//	                Runtime.getRuntime().exit(0);
	                break;
	        }
	    } while(ch != 0);
	    
	}
}