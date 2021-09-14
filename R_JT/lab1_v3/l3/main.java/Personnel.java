
public class Personnel extends WorkingMan {
    private double experience;
    private String position;
    public Personnel(int age, String fio, String sex, String position, double experience) {
        super(age, fio, sex);
        this.position = position;
        this.experience = experience;
        
    }
    public String getPosition() {
        return position;
    }
    public double getExperience() {
        return experience;
    }
    public String toString() {
        
        return String.format("%1s, %2s, %3s", super.toString(), position, experience);
    }
}