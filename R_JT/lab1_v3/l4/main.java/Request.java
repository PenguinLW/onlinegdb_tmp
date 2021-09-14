
public class Request {
    private String destination, flight_numb, name_pass;
    private int[] departure_date;
    
    public Request(String destination, String flight_numb, String name_pass, int[] departure_date) {
        this.destination = destination;
        this.flight_numb = flight_numb;
        this.name_pass = name_pass;
        this.departure_date = departure_date;
    }
    public String getFlightNumb() {
        
        return flight_numb;
    }
    public boolean checkDate(int[] sub_list) {
        boolean flag = false;
        for(int i = 0; i <= departure_date.length-1; i++) {
            if(departure_date[i] == sub_list[i]) {
                flag = true;
            } else {
                flag = false;
                break;
            }
        }
            
/*        if(departure_date.equals(sub_list)) {
            return true;
        } else {
            return false;
        }*/
        return flag;
    }
    public String toString() {
        
        return String.format("%1s, %2s, %3s, %4s:%5s:%6s", destination, flight_numb, name_pass, departure_date[0], departure_date[1], departure_date[2]);
    }
}