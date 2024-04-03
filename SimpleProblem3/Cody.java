package SimpleProblem3;

public class Main {

    public static void main(String[] args) {
  
      String[] arr = {"a", "b", "c", "d", "a", "c", "e"};
      
      List<String> filtered = new ArrayList<>();
  
      for(String str : arr) {
        if(!filtered.contains(str)) {
          filtered.add(str);
        }
      }
  
      String[] result = filtered.toArray(new String[0]);
  
      System.out.println(Arrays.toString(result));
    }
  }
