import java.net.*;
import java.util.*;
import java.io.*;
import java.nio.*;
import java.lang.*;
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
            //getting the credentials
            Scanner input = new Scanner(System.in);
            System.out.print("Username:- ");
            String username = input.nextLine();
            Console console = System.console();
            String password = new String(console.readPassword("Password:- "));
            //encryption logic
            StringBuilder sb = new StringBuilder();
            sb.append(username);
            sb.append(" ");
            sb.append(password);
            sb = sb.reverse();
            String output = sb.toString() + "\n";
            char[] str = output.toCharArray();
            for(int i = 0; i < str.length - 1; i++){
                str[i] = ((char) ~str[i]);
            }
            //done encrypting
 
            //Send the message to the server
            OutputStream os = socket.getOutputStream();
            OutputStreamWriter osw = new OutputStreamWriter(os);
            BufferedWriter bw = new BufferedWriter(osw);
            bw.write(str);
            bw.flush();
            //Get the return message from the server
            InputStream is = socket.getInputStream();
            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader br = new BufferedReader(isr);
            String message = br.readLine();
            System.out.println("Server >  " +message);
        }
        catch (Exception exception)
        {
            System.out.println(exception.getMessage());
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
