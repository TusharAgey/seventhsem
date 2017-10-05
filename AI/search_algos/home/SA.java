import java.util.*;
class SA{
    static int  K = 20;
    static int v = 10;
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter room temparture");
        int rt = sc.nextInt();
        System.out.println("Select the Material");
        System.out.println("1)Iron"); //1583
        System.out.println("2)Nikel");//1455
        System.out.println("3)Cobalt");//1495
        int choice = sc.nextInt();
        int mi = 1583;
        int mn = 1455;
        int mco = 1495;
        switch(choice){
            case 1:
                ann(rt,mi);
                break;
            case 2:
                ann(rt,mn);
                break;
            case 3:
                ann(rt,mco);
                break;
        }
    }
    public static void ann(int rt,int mt){
        int annt = mt;
        int rtt = rt;
        int r = 0;
        int count = 0;
        float t = 0;
        while(annt > rt ){
            rt = heat(rt);
            rt = cool(rt);
           count++;
           System.out.println(count);
        }
            r = count;
            float x = (1 / r);
             System.out.println(x);
            t = ((2000 * x) + rtt);
            System.out.print(t);
    }
    public static int heat(int rt){
         rt = rt + 30;
        return rt;
    }
    public static int cool(int rt){
        rt = rt - 10;
        return rt;
    }
}