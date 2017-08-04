import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.io.Console;
import java.util.Scanner;
import java.io.*;
import java.nio.*;
public class Client
{
    private static Socket socket;
    public static void main(String args[])
    {
        try
        {
            String host = "localhost";
            int port = 25000;
            InetAddress address = InetAddress.getByName(host);
            socket = new Socket(address, port);
            Scanner input = new Scanner(System.in);
            System.out.println("Username:- ");
            String username = input.nextLine();
              Console console = System.console();
            String password = new String(console.readPassword("Password:- "));
            Process p = Runtime.getRuntime().exec("echo \"" + username + " " + password + "\" >> data && ./encrypt data");
            p.waitFor();
            //Send the message to the server
            OutputStream os = socket.getOutputStream();
            OutputStreamWriter osw = new OutputStreamWriter(os);
            BufferedWriter bw = new BufferedWriter(osw);

            String sendMessage = new Scanner(new File("output.txt")).nextLine();
            sendMessage = sendMessage + "\n";
            bw.write(sendMessage);
            bw.flush();
            //Get the return message from the server
            InputStream is = socket.getInputStream();
            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader br = new BufferedReader(isr);
            String message = br.readLine();
            System.out.println("Message received from the server : " +message);
        }
        catch (Exception exception)
        {
            exception.printStackTrace();
        }
        finally
        {
            //Closing the socket
            try
            {
                socket.close();
            }
            catch(Exception e)
            {
                e.printStackTrace();
            }
        }
    }
}
