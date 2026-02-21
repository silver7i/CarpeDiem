import java.util.Scanner;

public class SWEA_1959_두개의숫자열 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			
			int n = sc.nextInt();
			int m = sc.nextInt();
			
			int[] nArr = new int[n];
			int[] mArr = new int[m];
			
			
			for(int i=0; i<n; i++) {
				nArr[i] = sc.nextInt();
			}
			
			for(int i=0; i<m; i++) {
				mArr[i] = sc.nextInt();
			}
			
			int max = 0;
			if(n < m) {
				
				for(int i=0; i<m; i++) {
					int sum = 0;
					for(int j=0; j<n; j++) {
						if((n-1)+i < m) {
							sum += nArr[j]*mArr[i+j];
						}
					}
					if(max < sum) max = sum;
				}
			}
			
			else if(n > m) {
				
				for(int i=0; i<n; i++) {
					int sum = 0;
					for(int j=0; j<m; j++) {
						if((m-1)+i < n) {
							sum += nArr[j+i]*mArr[j];
						}
					}
					if(max < sum) max = sum;
				}
			}
			
			else {
				int sum = 0;
				for(int i=0; i<n; i++) {
					sum += nArr[i] * mArr[i];
				}
				
				max = sum;
			}
			
			
			
		System.out.println("#"+tc+" "+max);
		}
		
	}
}
