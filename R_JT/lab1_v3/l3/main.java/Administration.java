
public class Administration extends Personnel {
    private String lev;
    public Administration(int age, String fio, String sex, String position, double experience, String lev) {
        super(age, fio, sex, position, experience);
        this.lev = lev;
    }
    public String getLev() {
        return lev;
    }
    public String toString() {
        
        return String.format("%1s, %2s", super.toString(), lev);
    }
}