import java.util.Scanner;

public class SWEA_2817_부분수열의합 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			
			int n = sc.nextInt();
			int k = sc.nextInt();
			
			int[] arr = new int[n];
			
			for(int i=0; i<n; i++) {
				arr[i] = sc.nextInt();
				
			}
			int cnt = 0;

			for(int i=0; i < (1 << n); i++) {
				int sum = 0;
				for(int j=0; j < n; j++) {
					
					if((i & (1 << j)) > 0) {
						sum += arr[j];
					}
					
				}
				if(sum == k) {
					cnt++;
				}
			}
			
			System.out.println("#"+tc+" "+cnt);
		}
	}
}
