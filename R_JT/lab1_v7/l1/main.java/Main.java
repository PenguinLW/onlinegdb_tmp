
import java.io.File;
// import java.io.FileInputStream;
// import java.io.FileOutputStream;
// import java.io.ByteArrayInputStream;
// import java.io.ByteArrayOutputStream;
// import java.io.BufferedInputStream;
// import java.io.BufferedOutputStream;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;
public class Main {
    private static File file;
    private static Scanner in;
    private static String rff(File file) {
        int symb;
        String abonent_out = "";
        FileReader ffr;
	    try {
            ffr = new FileReader(file);
            symb = ffr.read();
            while(symb != -1) {
    	        abonent_out += (char) symb;
    	        symb = ffr.read();
            }
    	    ffr.close();
	    } catch(FileNotFoundException exc) {
	        
	    } catch(IOException exc) {
	        
	    }
        
        return abonent_out;
    }
    private static void wtf(File file, String content) {
        FileWriter ffw;
	    try {
    	    ffw = new FileWriter(file);
    	    for(int i = 0; i <= content.length()-1; i++) {
    	        ffw.write(content.charAt(i));
    	    }
    	    ffw.close();
	    } catch(FileNotFoundException exc) {
	        
	    } catch(IOException exc) {
	        
	    }
    }
	public static void main(String[] args) {
	    int ch;
	    String[] list_ab, n_ab_list;
	    
	    file = new File("list_abonents.txt");
	    in = new Scanner(System.in);
	    
//	    create_ab_list(file);
        list_ab = rff(file).split("\n");
        n_ab_list = new String[list_ab.length];
        for(int i = 0; i <= list_ab.length-1; i++) {
            n_ab_list[i] = list_ab[i].split("\t")[1];
        }
        
        do {
            System.out.println("1. Задать фамилию для поиска абонента\n0. Выход");
            ch = in.nextInt();
            switch(ch) {
                case 1:
                    int index;
                    String rez;
                    System.out.println("Выберите фамилию:");
                    for(int i = 0; i <= n_ab_list.length-1; i++) {
                        System.out.println("\t"+(i+1)+"\t"+n_ab_list[i]);
                    }
                    index = in.nextInt();
                    if(index > 0 && index <= list_ab.length) {
                        rez = "По заданному имени ("+n_ab_list[index-1]+") отысканы следующие контактные данные:\n\t"+list_ab[index-1];
                        wtf(new File("rezults.txt"), list_ab[index-1]);
                        System.out.println(rez+"\nРезультат можно просмотреть после завершения работы программы в файле results.txt");
                        
                    } else {
                        System.out.println("Вы ошиблись в выборе адреса, попробуйте ещё раз.");
                    }
                    break;
                default:
                    ch = 0;
//                    Runtime.getRuntime().exit(0);
                    break;
            }
        } while(ch != 0);
	}
	private static void create_ab_list(File file) {
        String abonent_in = ""+
        "+79000000001\tLaura Team\tBrodway St. 71\n"+
        "+79010000002\tShery Bounce\tGolliw St. 71\n"+
        "+79020000003\tInga Lead\tNizhnya Naberezhnya St. 12a\n"+
        "+79030000004\tCorvy Sider\tCanalis St. 8\n"+
        "+79040000005\tRaw Edge\tMountain St. 77\n"+
        "+79050000006\tHugo Boss\tItalyan St. 999\n"+
        "+79060000007\tGenry Octal\tGeometry St. 0\n"+
        "+79070000008\tUn Cho\tYorkname St. 4\n"+
        "+79080000009\tLi Shiyan\tNegrot St. 1\n"+
        "+79090000010\tJack Chan\tShansh St. 71\n"+
        "+79100000011\tIndi Apolis\tLidni St. 10\n"+
        "+79110000012\tJeffry Barateon\tVisoko St. 7\n"+
        "+79120000013\tSergey Bezrukov\tShalyapina St. 9\n"+
        "+79130000014\tVladimir Putin\tLenina St. 91\n";
        wtf(file, abonent_in);
	    
	}
}
