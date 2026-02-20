import java.util.Scanner;

public class BOJ_1003_피보나치함수 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int[][] fibo = new int[50][2];
		
		fibo[0] = new int[] {1, 0}; 
		fibo[1] = new int[] {0, 1}; 
		
		for(int i=2; i<50; i++) {
			fibo[i] = new int[] {(fibo[i-1][0] + fibo[i-2][0]), (fibo[i-1][1] + fibo[i-2][1])};
		}
		
		int n = sc.nextInt();
		for(int i=0; i<n; i++) {
			int k = sc.nextInt();
			System.out.println(fibo[k][0]+" "+fibo[k][1]);
		}
		
	}
}
