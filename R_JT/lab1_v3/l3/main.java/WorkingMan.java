
public class WorkingMan {
    private int age;
    private String fio, sex;
    public WorkingMan(int age, String fio, String sex) {
        this.fio = fio;
        this.age = age;
        this.sex = sex;
    }
    public int getAge() {
        return age;
    }
    public String getFio() {
        return fio;
    }
    public String getSex() {
        return sex;
    }
    public String toString() {
        
        return String.format("%1s, %2s, %3s", age, fio, sex);
    }
}