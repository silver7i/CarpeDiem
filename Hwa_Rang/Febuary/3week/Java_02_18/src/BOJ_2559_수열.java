import java.util.Scanner;

public class BOJ_2559_수열 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		int[] arr = new int[n];
		
		for(int i=0; i<n; i++) {
			arr[i] = sc.nextInt();
		}
		
		int max = Integer.MIN_VALUE;
		
		for(int i=0; i<n; i++) {
			int sum = 0;
			boolean isChanged = false;
			if(i+k<=n) {
				isChanged = true;
				for(int j=i; j<i+k; j++) {
					sum += arr[j];
				}
			}			
			if(max < sum && isChanged) max = sum;
		}

		System.out.println(max);
	}
}
