import java.io.*;
import java.net.*;

public class ServeurUDP {
    public static void main(String[] args) {
        try {
            DatagramSocket sock = new DatagramSocket(1234);
            while (true) {
                byte[] buffer = new byte[1024];
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                sock.receive(packet); 

                String receivedMessage = new String(packet.getData(), 0, packet.getLength());
                System.out.println("Message reçu: " + receivedMessage);

                InetAddress addr = packet.getAddress();
                int clientPort = packet.getPort();
                DatagramPacket responsePacket = new DatagramPacket(packet.getData(), packet.getLength(), addr, clientPort);
                sock.send(responsePacket);
                System.out.println("Message renvoyé au client: " + receivedMessage);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

