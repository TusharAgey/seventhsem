import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.*;
import java.io.*;
import java.nio.*;
public class Server
{

    private static Socket socket;

    public static void main(String[] args)
    {
        try
        {

            int port = 25000;
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Server Started and listening to the port 25000");

            //Server is running always. This is done using this while(true) loop
            while(true)
            {
                //Reading the message from the client
                socket = serverSocket.accept();
                InputStream is = socket.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                BufferedReader br = new BufferedReader(isr);
                String credentials = br.readLine();
                Process p = Runtime.getRuntime().exec("echo \"" + credentials + "\" >> output && ./decrypt output");
                p.waitFor();
                String sendMessage = new Scanner(new File("final_data.txt")).nextLine();
                String returnMessage;
                returnMessage = sendMessage;
                if(sendMessage.contains("Tushar") && sendMessage.contains("qwerty")){
                  returnMessage += " Authenticated\n";
                }
                else
                  returnMessage += " Authentication failed\n";
                //Multiplying the number by 2 and forming the return message

                //Sending the response back to the client.
                OutputStream os = socket.getOutputStream();
                OutputStreamWriter osw = new OutputStreamWriter(os);
                BufferedWriter bw = new BufferedWriter(osw);
                bw.write(returnMessage);
                System.out.println("Message sent to the client is "+returnMessage);
                bw.flush();
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                socket.close();
            }
            catch(Exception e){}
        }
    }
}
