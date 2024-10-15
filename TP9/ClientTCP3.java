import java.io.*;
import java.net.*;

public class ClientTCP3 
{
    public static void main(String[] args) throws IOException 
  {
        Socket socket = new Socket("localhost", 2016);
        System.out.println("Connexion d'un client");

        DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());
        DataInputStream dIn = new DataInputStream(socket.getInputStream());

        String messageToSend = args.length > 0 ? args[0] : "message test";
        dOut.writeUTF(messageToSend);
        dOut.flush();

        String reversedMessage = dIn.readUTF();
        System.out.println("Message inversé reçu du serveur: " + reversedMessage);

        socket.close();
  }
}

