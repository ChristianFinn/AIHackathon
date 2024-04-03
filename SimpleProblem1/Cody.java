import com.fasterxml.jackson.databind.ObjectMapper;

public class Main {

  public static void main(String[] args) throws IOException {
    
    String json = "{\"name\":\"John\", \"age\":30, \"car\":volvo}";

    ObjectMapper mapper = new ObjectMapper();
    User user = mapper.readValue(json, User.class);
    
    System.out.println(user);
  }
}

class User {

  public String name;
  public int age;
  public Car car;

  // Getters, setters, toString
  
}

class Car {

  public String model;
  public int year;
  
  // Getters, setters, toString 
}