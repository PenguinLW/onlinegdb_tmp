
public class Test {
    private String dt, aud;
    public Test(String dt, String aud) {
        this.dt = dt;
        this.aud = aud;
    }
    public String getDateTime() {
        return dt;
    }
    public String getAuditories() {
        return aud;
    }
    public String toString() {
        return String.format("%1$s, %2$s", dt, aud);
    }
}