
public class Bus {
    private String num_bus, driver_name, num_route;
    public Bus(String num_bus, String driver_name, String num_route) {
        this.num_bus = num_bus;
        this.driver_name = driver_name;
        this.num_route = num_route;
    }
    public String getNumBus() {
        return num_bus;
    }
    public String toString() {
        return String.format("%1$10s\t%2$30s\t%3$5s", num_bus, driver_name, num_route);
    }
}