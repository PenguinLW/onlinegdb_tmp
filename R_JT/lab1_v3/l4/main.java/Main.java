
import java.util.Scanner;
import java.util.ArrayList;
public class Main {
    private static Scanner in;
    private static ArrayList<Request> req;
    
    private static String show_req() {
        String str = "";
        for(int i = 0; i <= req.size()-1; i++) {
            str += "\t"+(i+1)+"\t"+req.get(i)+"\n";
        }
        return str;
    }
    private static void add_req() {
        String destination, flight_numb, name_pass;
        String[] departure_date;
        
        System.out.println("Укажите направление:");
        in.nextLine();
        destination = in.nextLine();
        System.out.println("Укажите номер рейса:");
        flight_numb = in.nextLine();
        System.out.println("Фамилия и инициалы:");
        name_pass = in.nextLine();
        System.out.println("Желаемая дата вылета (числами, разделяя двоеточием):");
        departure_date = (in.nextLine()).split(":");
        req.add(new Request(
            destination,
            flight_numb,
            name_pass,
            new int[]{
                    Integer.parseInt(departure_date[0]),
                    Integer.parseInt(departure_date[1]),
                    Integer.parseInt(departure_date[2])
                }
            )
        );
    }
    private static void del_req(int index) {
        
        req.remove(index-1);
    }
    private static String find_req(String[] kroff) {
        String str = "";
        String[] ddate = kroff[1].split(":");
        ArrayList<Request> sub_list = new ArrayList<Request>();
        for(int i = 0; i <= req.size()-1; i++) {
            if((req.get(i).getFlightNumb()).equals(kroff[0])) {
                sub_list.add(req.get(i));
            }
        }
        for(int i = 0; i <= sub_list.size()-1; i++) {
            
            if(!(sub_list.get(i)).checkDate(new int[]{
                    Integer.parseInt(ddate[0]),
                    Integer.parseInt(ddate[1]),
                    Integer.parseInt(ddate[2])
                }
            )) {
                sub_list.remove(i);
            } else {
                str += "\t"+sub_list.get(i).toString()+"\n";
            }
        }
        return str;
    }
	public static void main(String[] args) {
	    int ch;
	    in = new Scanner(System.in);
	    req = new ArrayList<Request>();
	    
	    do {
	        System.out.println("1. Добавить заявку\n2. Отобразить существующие заявки\n3. Удаление заявки\n4. Поиск по заявкам\n0. Выход");
	        ch = in.nextInt();
	        switch(ch) {
	            case 1:
	                add_req();
	                break;
                case 2:
                    System.out.println(show_req());
                    break;
                case 3:
                    System.out.println("Укажите номер удаляемой заявки:");
                    try {
                        del_req(in.nextInt());
                        
                    } catch(IndexOutOfBoundsException exc) {
                        System.out.println("Такой заявки не существует. Будьте внимательны при выборе.");
                    }
                    break;
                case 4:
                    System.out.println("Укажите номер рейса и дату (числами, разделяя двоеточием):");
                    in.nextLine();
                    System.out.println(find_req(in.nextLine().split(" ")));
                    break;
                default:
                    ch = 0;
                    break;
	        }
	        
	    } while(ch != 0);
	    
	    
	}
}