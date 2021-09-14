
public class Proving extends Exam {
    private String degree, lev;
    public Proving(String dt, String aud,  String degree, String lev) {
        super(dt, aud, "испытание освоенных навыков на практике");
        this.degree = degree;
        this.lev = lev;
    }
    public String getDegree() {
        return degree;
    }
    public String getLev() {
        return lev;
    }
    public String toString() {
        return String.format("%1$s, %2$s, %3$s", super.toString(), degree, lev);
    }
}