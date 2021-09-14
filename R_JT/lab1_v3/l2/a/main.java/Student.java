
public class Student {
    private String fio, group;
    private double av_count, many;
    public Student(String fio, String group, double av_count, double many) {
        this.fio = fio;
        this.group = group;
        this.av_count = av_count;
        this.many = many;
    }
    public double getAvCount() {
        return av_count;
    }
    public double getMany() {
        return many;
    }
    public String toString() {
        
        return String.format("Student: %1$s\t%2$s\t%3$s\t%4$s", this.fio, this.group, this.av_count, this.many);
    }
    
}