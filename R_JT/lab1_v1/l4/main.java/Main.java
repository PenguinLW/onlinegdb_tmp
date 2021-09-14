
import java.util.Scanner;
import java.util.ArrayList;
public class Main {
    private static Scanner in;
    private static ArrayList<Bus> bus_inthe_park, bus_outsidethe_park;
    private static String data_ofthe_bus_park = "e401mk\tGregory House\t16k\n"+
                                            "r707gg\tTonny White\t417\n"+
                                            "u301dt\tRenchen Boldaev\t80r\n"+
                                            "y765ui\tOlga Zevagaradnye\t480\n"+
                                            "y764tr\tKonstantin Maslyakov\t45\n"+
                                            "l441lk\tSergey Tyrskiyx\t55e\n"+
                                            "u777il\tFedor Haskell\t4k\n"+
                                            "i092mb\tPetro Tretyakov\t120k\n"+
                                            "g676hh\tIgor Emelyanenkov\t446b\n";
    private static void init_park() {
	    String[]  dobp = data_ofthe_bus_park.split("\n");
	    for(int i = 0; i <= dobp.length-1; i++) {
	        String[] dob = dobp[i].split("\t");
	        bus_inthe_park.add(new Bus(dob[0], dob[1], dob[2]));
	    }
    }
    private static String show_park() {
        String str = "";
        if(bus_inthe_park.size() != 0) {
            for(int i = 0; i <= bus_inthe_park.size()-1; i++) {
                str += (bus_inthe_park.get(i)).toString()+"\n";
            }
        } else {
            str += "Все автобусы на маршрутах.";
        }
        return String.format("%1s",str);
    }
    private static String show_route() {
        String str = "";
        if(bus_outsidethe_park.size() != 0) {
            for(int i = 0; i <= bus_outsidethe_park.size()-1; i++) {
                str += (bus_outsidethe_park.get(i)).toString()+"\n";
            }
        } else {
            str += "Все автобусы в парке.";
        }
        return String.format("%1s", str);
    }
    private static void add_to_route(String num_bus) {
        boolean flag = false;
        for(int i = 0; i <= bus_inthe_park.size()-1; i++) {
            if(num_bus.equals((bus_inthe_park.get(i)).getNumBus())) {
                bus_outsidethe_park.add(bus_inthe_park.get(i));
                bus_inthe_park.remove(i);
                System.out.println("Автобус успешно добавлен на маршрут.");
                flag = true;
            }
        }
        if(!flag) {
            System.out.println("Автобуса с таким гос. рег. номером не существует. Попробуйте ещё раз");
        }
    }
    private static void remove_from_route(String num_bus) {
        boolean flag = false;
        for(int i = 0; i <= bus_outsidethe_park.size()-1; i++) {
            if(num_bus.equals((bus_outsidethe_park.get(i)).getNumBus())) {
                bus_inthe_park.add(bus_outsidethe_park.get(i));
                bus_outsidethe_park.remove(i);
                System.out.println("Автобус успешно удалён с маршрута.");
                flag = true;
            }
        }
        if(!flag) {
            System.out.println("Автобуса с таким гос. рег. номером не существует. Попробуйте ещё раз");
        }
    }
	public static void main(String[] args) {
	    int ch;
	    in = new Scanner(System.in);
	    bus_inthe_park = new ArrayList<Bus>();
	    bus_outsidethe_park = new ArrayList<Bus>();
	    init_park();
	    do {
	        System.out.println("1. Постановка автобуса на маршрут\n2. Удаление автобуса с маршрута\n3. Вывести список автобусов на маршрутах\n4. Вывести список всех автобусов в парке\n0. Выход");
	        ch = in.nextInt();
	        switch(ch) {
	            case 1:
	                System.out.println("Введите гос. рег. номер автобуса:");
	                in.nextLine();
	                add_to_route(in.nextLine().toLowerCase());
	                break;
	            case 2:
	                System.out.println("Введите гос. рег. номер автобуса:");
	                in.nextLine();
	                remove_from_route(in.nextLine().toLowerCase());
	                break;
	            case 3:
	                System.out.println(show_route());
	                break;
	            case 4:
	                System.out.println(show_park());
	                break;
	            case 0:
	                ch = 0;
//                    Runtime.getRuntime().exit(0);
	                break;
	        }
	    } while(ch != 0);
	    
	}
}