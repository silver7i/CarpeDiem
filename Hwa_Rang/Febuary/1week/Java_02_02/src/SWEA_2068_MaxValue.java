import java.util.Scanner;
 
public class SWEA_2068_MaxValue {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
         
        int t = sc.nextInt();
        for(int i=1; i<=t; i++) {
             
            int max = 0;
            for(int j=0; j<10; j++) {
                int n = sc.nextInt();
                if(max<n) max=n;
            }
             
            System.out.println("#"+i+" "+max);
                         
             
        }
    }
 
}