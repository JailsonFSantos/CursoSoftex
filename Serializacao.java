//Serializacao
 
 
 FileOutputStream fileStream = new FileOutputStream("MyJava.teste");
 ObjectOutputStream obj = new ObjectOutputStream(fileStream);
 
 obj.writeObject(JavaUM);
 obj.writeObject(JavaDOIS); 

 obj.close;


//Deserializacao


 FileInputStream fileStream = new FileInputStream("MyJava.teste");
 ObjectInputStream os = new ObjectInputStream(fileStream);

 Object um = obj.readObject();
 Object dois = obj.readObject();

 ObjetoJava teste   = (Java) um;
 ObjetoJava teste_2 = (Java) dois;

 os.close();