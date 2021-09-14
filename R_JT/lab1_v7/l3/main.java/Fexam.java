
public class Fexam extends Exam {
    private String degree;
    public Fexam(String dt, String aud, String form, String degree) {
        super(dt, aud, form);
        this.degree = degree;
    }
    public String getDegree() {
        return degree;
    }
    public String toString() {
        return String.format("%1$s, %2$s", super.toString(), degree);
    }
}