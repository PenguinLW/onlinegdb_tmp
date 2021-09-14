
public class Engineer extends Personnel {
    private String lev;
    public Engineer(int age, String fio, String sex, double experience, String lev) {
        super(age, fio, sex, "service-engineer", experience);
        this.lev = lev;
    }
    public String getLev() {
        return lev;
    }
    public String toString() {
        
        return String.format("%1s, %2s", super.toString(), lev);
    }
}