package java_tests;

@Test
public void testJSONMapping() throws IOException {

  String json = "{\"name\":\"John\", \"age\":30}";
  
  ObjectMapper mapper = new ObjectMapper();
  User user = mapper.readValue(json, User.class);

  assertEquals("John", user.getName());
  assertEquals(30, user.getAge());
}

@Test 
public void testJSONFromFile() throws IOException {

  ObjectMapper mapper = new ObjectMapper();
  User user = mapper.readValue(new File("user.json"), User.class);
  
  assertEquals("Expected Name", user.getName());
  assertEquals(Expected Age, user.getAge());
}
