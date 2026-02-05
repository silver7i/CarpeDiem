import java.util.Scanner;
 
class SWEA_1984_Mid_Avg_Value
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
     
 
        for(int test_case = 1; test_case <= T; test_case++)
        {
         
            int sum = 0;
        int max = 0;
        int min = 10000;
        for(int i=0; i<10; i++) {
        int n = sc.nextInt(); 
            if(max<n) max = n;
            if(min>n) min = n;
            sum += n;
        }
        double total = ((sum-max-min) / 8.0);
        System.out.printf("#%d %d\n", test_case, Math.round(total));
 
        }
    }
}