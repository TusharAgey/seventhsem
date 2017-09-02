import java.net.*;
import java.lang.*;
import java.util.*;
import java.io.*;
import java.nio.file.Files;
class Stego{
    private static void insertIntoImage() throws Exception{
        System.out.print("Enter the input image name:");
        File fi = new File(new Scanner(System.in).nextLine());
        byte[] data = Files.readAllBytes(fi.toPath());
        System.out.print("Enter the name of the file to hide:");
        File ip_file = new File(new Scanner(System.in).nextLine());
        byte[] buffer = Files.readAllBytes(ip_file.toPath());
        int siz = buffer.length;
        int len = data.length;
        FileOutputStream wr = new FileOutputStream("newestImage.jpg");
        int i = 0;
        while(i < 1100){
            wr.write(data[i]);
            i++;
        }
        int j = 0;
        wr.write((byte)siz);
        i++;
        while((i < len) && (j < siz)){
            if(i > siz){
                wr.write(buffer[j]);
                j++;
                i++;
            }
            wr.write(data[i]);
            i++;
        }
        while(i < len)
            wr.write(data[i++]);
        wr.close();
    }
    public static void retrieveData() throws Exception{
        System.out.println("Enter the input image name:");
        File fi = new File(new Scanner(System.in).nextLine());
        byte[] data = Files.readAllBytes(fi.toPath());
        int len = data.length;
        int i = 1100;
        int j = 0;
        int siz = data[i];
        i++;
        while((i < len) && (j < siz)){
            if(i > siz){
                System.out.print((char)data[i]);
                j++;
                i++;
            }
            i++;
        }
    }
    public static void main(String args[])throws Exception{
        System.out.println("Enter 1 to embedd data into image, 2 to retrieve data from an image");
        if(new Scanner(System.in).nextInt() == 1){
            insertIntoImage();
        }
        else
            retrieveData();
    }
}