import java.io.*;
import java.net.*;

public class Clienthttp {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java Clienthttp <hostname>");
            return;
        }

        String hostname = args[0];
        int port = 80;

        try (
            Socket socket = new Socket(hostname, port);

            OutputStreamWriter osw = new OutputStreamWriter(socket.getOutputStream());
            InputStreamReader isw = new InputStreamReader(socket.getInputStream());
            BufferedWriter bufOut = new BufferedWriter(osw);
            BufferedReader bufIn = new BufferedReader(isw)
        ) {
            // Envoi de la requête HTTP GET
            String request = "GET / HTTP/1.0\r\n\r\n";
            bufOut.write(request, 0, request.length());
            bufOut.flush();

            // Lecture de la réponse et affichage du contenu HTML
            String line;
            while ((line = bufIn.readLine()) != null) {
                System.out.println(line);
            }

        } catch (UnknownHostException e) {
            System.err.println("Hôte inconnu : " + hostname);
        } catch (IOException e) {
            System.err.println("Erreur d'E/S : " + e.getMessage());
        }
    }
}

