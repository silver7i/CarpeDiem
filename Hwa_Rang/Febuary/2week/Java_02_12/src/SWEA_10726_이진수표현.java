import java.util.Scanner;

public class SWEA_10726_이진수표현 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		for(int tc=1; tc<=t; tc++) {

			int n = sc.nextInt();
			int m = sc.nextInt();
			
			if((m & ((1 << n)-1)) == ((1 << n)-1)){
				System.out.println("#"+tc+" ON");
			}else {
				System.out.println("#"+tc+" OFF");				
			}
		}
	}
}
