import java.util.Scanner;

public class SWEA_1217_거듭제곱 {
	static int loopX(int n, int m) {
		if(m==1) {
			return n;
		}
		return n * loopX(n, m-1);
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int tc=1; tc<=10; tc++) {
			int t = sc.nextInt();
			int n = sc.nextInt();
			int m = sc.nextInt();
			
			System.out.println("#"+t+" "+loopX(n, m));
		}
		
	}
}
