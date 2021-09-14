
public class Exam extends Test {
    private String form;
    public Exam(String dt, String aud, String form) {
        super(dt, aud);
        this.form = form;
    }
    public String getForm() {
        return form;
    }
    public String toString() {
        return String.format("%1$s, %2$s", super.toString(), form);
    }
}