
public class Participant {
    private int age;
    private double height, weight;
    private String country_nm, team_nm, gaming_number, fio;
    public Participant(String country_nm, String team_nm, String gaming_number, String fio, int age, double height, double weight) {
        this.country_nm = country_nm;
        this.team_nm = team_nm;
        this.gaming_number = gaming_number;
        this.fio = fio;
        this.age = age;
        this.height = height;
        this.weight = weight;
    }
    public int getAge() {
        return age;
    }
    public double getHeight() {
        return height;
    }
    public double getWeight() {
        return weight;
    }
    public String getTeamNm() {
        return team_nm;
    }
    public String toString() {
        return String.format("\t%1$s\t%2$s\t%3$s\t%4$s\t%5$s\t%6$s\t%7$s",country_nm, team_nm, gaming_number, fio, age, height, weight);
    }
}