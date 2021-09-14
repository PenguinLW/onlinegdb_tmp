
public class Auto {
    private String cnumb, ccolor, cmake, cmodel;
    private int used;
    public Auto(String cnumb, String ccolor, String cmake, String cmodel) {
        used = 0;
        this.cnumb = cnumb;
        this.ccolor = ccolor;
        this.cmake = cmake;
        this.cmodel = cmodel;
    }
    public void setUsed() {
        used++;
    }
    public int getUsed() {
        return used;
    }
    public String getNumb() {
        return cnumb;
    }
    public String getColor() {
        return ccolor;
    }
    public String getMake() {
        return cmake;
    }
    public String getModel() {
        return cmodel;
    }
    public String toString() {
        return String.format("\t%1$s, %2$s, %3$s, %4$s\n\tВаша машина \"уступала дорогу\" %5$s раз", cnumb, ccolor, cmake, cmodel, used);
    }
}