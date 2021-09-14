
import java.util.Scanner;
import java.util.ArrayList;
public class Main {
    private static Scanner in;
    private static ArrayList<Participant> prpt;
    private static ArrayList<String> coteam;
    
    private static String show_prpt() {
        String stroka;
        stroka = "";
        for(int i = 0; i <= prpt.size()-1; i++) {
            stroka += (prpt.get(i))+"\n";
        }
        return stroka;
    }
    private static void collect_all_team() {
        
        for(int i = 0; i <= prpt.size()-1; i++) {
            if(!check_of_team((prpt.get(i)).getTeamNm())) {
                coteam.add((prpt.get(i)).getTeamNm());
            }
        }
    }
    private static boolean check_of_team(String nteam) {
        boolean flag = false;
        for(int i = 0; i <= coteam.size()-1; i++) {
            if((coteam.get(i)).equals(nteam)) {
                flag = true;
            }
        }
        return flag;
        
    }
    private static void sorted_of_age() {
        collect_all_team();
        ArrayList<Double> avrg_of_team = new ArrayList<Double>();
        ArrayList<String> sub_list_nt = new ArrayList<String>();
        ArrayList<Participant> sub_list_prpt = new ArrayList<Participant>();
        for(int i = 0; i <= coteam.size()-1; i++) {
            int count = 0, summ = 0;
            for(int j = 0; j <= prpt.size()-1; j++) {
                if((coteam.get(i)).equals((prpt.get(j)).getTeamNm())) {
                    summ += (prpt.get(j)).getAge();
                    count++;
                }
            }
            avrg_of_team.add(0.0+(summ/(count * 3)));
        }
        
        int i = 0, j = 0;
        while(coteam.size() > 0) {
            int index = 0;
            double min = avrg_of_team.get(index);
            while(j <= coteam.size()-1) {
                if(avrg_of_team.get(j) < avrg_of_team.get(index)) {
                    index = j;
                }
                j++;
            }
            sub_list_nt.add(coteam.get(index));
            coteam.remove(index);
            avrg_of_team.remove(index);
        }
        for(int k = 0; k <= sub_list_nt.size()-1; k++) {
            coteam.add(sub_list_nt.get(k));
        }
        sub_list_nt.clear();
        avrg_of_team.clear();
        for(int k = 0; k <= coteam.size()-1; k++) {
            for(int c = 0; c <= prpt.size()-1; c++) {
                if((coteam.get(k)).equals((prpt.get(c)).getTeamNm())) {
                    sub_list_prpt.add(prpt.get(c));
                }
            }
        }
        prpt.clear();
        for(int k = 0; k <= sub_list_prpt.size()-1; k++) {
            prpt.add(sub_list_prpt.get(k));
            System.out.println(sub_list_prpt.get(k));
        }
        sub_list_prpt.clear();
        
        
    }
    private static void sorted_of_height() {
        collect_all_team();
        ArrayList<Double> avrg_of_team = new ArrayList<Double>();
        ArrayList<String> sub_list_nt = new ArrayList<String>();
        ArrayList<Participant> sub_list_prpt = new ArrayList<Participant>();
        for(int i = 0; i <= coteam.size()-1; i++) {
            int count = 0, summ = 0;
            for(int j = 0; j <= prpt.size()-1; j++) {
                if((coteam.get(i)).equals((prpt.get(j)).getTeamNm())) {
                    summ += (prpt.get(j)).getHeight();
                    count++;
                }
            }
            avrg_of_team.add(0.0+(summ/(count * 3)));
        }
        
        int i = 0, j = 0;
        while(coteam.size() > 0) {
            int index = 0;
            double min = avrg_of_team.get(index);
            while(j <= coteam.size()-1) {
                if(avrg_of_team.get(j) > avrg_of_team.get(index)) {
                    index = j;
                }
                j++;
            }
            sub_list_nt.add(coteam.get(index));
            coteam.remove(index);
            avrg_of_team.remove(index);
        }
        for(int k = 0; k <= sub_list_nt.size()-1; k++) {
            coteam.add(sub_list_nt.get(k));
        }
        sub_list_nt.clear();
        avrg_of_team.clear();
        for(int k = 0; k <= coteam.size()-1; k++) {
            for(int c = 0; c <= prpt.size()-1; c++) {
                if((coteam.get(k)).equals((prpt.get(c)).getTeamNm())) {
                    sub_list_prpt.add(prpt.get(c));
                }
            }
        }
        prpt.clear();
        for(int k = 0; k <= sub_list_prpt.size()-1; k++) {
            prpt.add(sub_list_prpt.get(k));
            System.out.println(sub_list_prpt.get(k));
        }
        sub_list_prpt.clear();
        
        
    }
    private static void sorted_of_weight() {
        collect_all_team();
        ArrayList<Double> avrg_of_team = new ArrayList<Double>();
        ArrayList<String> sub_list_nt = new ArrayList<String>();
        ArrayList<Participant> sub_list_prpt = new ArrayList<Participant>();
        for(int i = 0; i <= coteam.size()-1; i++) {
            int count = 0, summ = 0;
            for(int j = 0; j <= prpt.size()-1; j++) {
                if((coteam.get(i)).equals((prpt.get(j)).getTeamNm())) {
                    summ += (prpt.get(j)).getWeight();
                    count++;
                }
            }
            avrg_of_team.add(0.0+(summ/(count * 3)));
        }
        
        int i = 0, j = 0;
        while(coteam.size() > 0) {
            int index = 0;
            double min = avrg_of_team.get(index);
            while(j <= coteam.size()-1) {
                if(avrg_of_team.get(j) < avrg_of_team.get(index)) {
                    index = j;
                }
                j++;
            }
            sub_list_nt.add(coteam.get(index));
            coteam.remove(index);
            avrg_of_team.remove(index);
        }
        for(int k = 0; k <= sub_list_nt.size()-1; k++) {
            coteam.add(sub_list_nt.get(k));
        }
        sub_list_nt.clear();
        avrg_of_team.clear();
        for(int k = 0; k <= coteam.size()-1; k++) {
            for(int c = 0; c <= prpt.size()-1; c++) {
                if((coteam.get(k)).equals((prpt.get(c)).getTeamNm())) {
                    sub_list_prpt.add(prpt.get(c));
                }
            }
        }
        prpt.clear();
        for(int k = 0; k <= sub_list_prpt.size()-1; k++) {
            prpt.add(sub_list_prpt.get(k));
            System.out.println(sub_list_prpt.get(k));
        }
        sub_list_prpt.clear();
        
        
    }
/*
    private static void sorted_of_light() {
        collect_all_team();
        ArrayList<Double> avrg_of_team = new ArrayList<Double>();
        ArrayList<String> sub_list_nt = new ArrayList<String>();
        ArrayList<Participant> sub_list_prpt = new ArrayList<Participant>();
        for(int i = 0; i <= coteam.size()-1; i++) {
            int count = 0, summ = 0;
            for(int j = 0; j <= prpt.size()-1; j++) {
                if((coteam.get(i)).equals((prpt.get(j)).getTeamNm())) {
                    summ += (prpt.get(j)).getAge()+(prpt.get(j)).getHeight()+(prpt.get(j)).getWeight();
                    count++;
                }
            }
            avrg_of_team.add(0.0+(summ/(count * 3)));
        }
        
        int i = 0, j = 0;
        while(coteam.size() > 0) {
            int index = 0;
            double min = avrg_of_team.get(index);
            while(j <= coteam.size()-1) {
                if(avrg_of_team.get(j) < avrg_of_team.get(index)) {
                    index = j;
                }
                j++;
            }
            sub_list_nt.add(coteam.get(index));
            coteam.remove(index);
            avrg_of_team.remove(index);
        }
        for(int k = 0; k <= sub_list_nt.size()-1; k++) {
            coteam.add(sub_list_nt.get(k));
        }
        sub_list_nt.clear();
        avrg_of_team.clear();
        for(int k = 0; k <= coteam.size()-1; k++) {
            for(int c = 0; c <= prpt.size()-1; c++) {
                if((coteam.get(k)).equals((prpt.get(c)).getTeamNm())) {
                    sub_list_prpt.add(prpt.get(c));
                }
            }
        }
        prpt.clear();
        for(int k = 0; k <= sub_list_prpt.size()-1; k++) {
            prpt.add(sub_list_prpt.get(k));
            System.out.println(sub_list_prpt.get(k));
        }
        sub_list_prpt.clear();
        
    }
*/
    private static String show_lteam() {
        String stroka = "";
        for(int i = 0; i <= prpt.size()-1; i++) {
            if((coteam.get(0)).equals((prpt.get(i)).getTeamNm())) {
                stroka += (prpt.get(i))+"\n";
            }
        }
        
        return stroka;
    }
    public static void main(String[] args) {
        in = new Scanner(System.in);
        prpt = new ArrayList<Participant>();
        coteam = new ArrayList<String>();
        int ch;
        do {
            System.out.println("1. Добавление участника\n2. Показать всех участников\n3. Показать молодую команду\n4. Показать команду самых высоких\n5. Показать команду самых легких (в весе)\n0. Выход");
            ch = in.nextInt();
            switch(ch) {
                case 1:
                    int age;
                    double height, weight;
                    String country_nm, team_nm, gaming_number, fio;
                    System.out.println("Укажите данные об участнике:");
                    in.nextLine();
                    System.out.print("Страна: ");
                    country_nm = in.nextLine();
                    System.out.print("Команда: ");
                    team_nm = in.nextLine();
                    System.out.print("Игровой номер: ");
                    gaming_number = in.nextLine();
                    System.out.print("Имя: ");
                    fio = in.nextLine();
                    System.out.print("Возраст: ");
                    age = in.nextInt();
                    System.out.print("Рост: ");
                    height = in.nextFloat();
                    System.out.print("Вес: ");
                    weight = in.nextDouble();
                    prpt.add(new Participant(country_nm, team_nm, gaming_number, fio, age, height, weight));
//                    System.out.println(prpt.get(prpt.size()-1));
//                    sorted_of_light();
                    break;
                case 2:
                    System.out.println(show_prpt());
                    break;
                case 3:
                    sorted_of_age();
//                    System.out.println(show_lteam());
                    break;
                case 4:
                    sorted_of_height();
//                    System.out.println(show_lteam());
                    break;
                case 5:
                    sorted_of_weight();
//                    System.out.println(show_lteam());
                    break;
                default:
                    ch = 0;
//                    Runtime.getRuntime().exit(0);
                    break;
            }
            
        } while(ch != 0);
    }
}
