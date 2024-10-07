import java.io.*;
import java.net.*;

public class ClientUDP {
    public static void main(String[] args) {
        try {
            DatagramSocket sock = new DatagramSocket();
            String messageToSend = "Hello, Server!";
            byte[] dataToSend = messageToSend.getBytes();

            InetAddress addr = InetAddress.getByName("localhost");
            DatagramPacket packetToSend = new DatagramPacket(dataToSend, dataToSend.length, addr, 1234);
            sock.send(packetToSend); 
            System.out.println("Message envoyé: " + messageToSend);

            byte[] buffer = new byte[1024];
            DatagramPacket responsePacket = new DatagramPacket(buffer, buffer.length);
            sock.receive(responsePacket); 

            String receivedResponse = new String(responsePacket.getData(), 0, responsePacket.getLength());
            System.out.println("Réponse reçue du serveur: " + receivedResponse);
            sock.close(); 
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

