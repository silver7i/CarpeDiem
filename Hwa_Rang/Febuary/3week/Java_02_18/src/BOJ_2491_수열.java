import java.util.Scanner;

public class BOJ_2491_수열 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] arr = new int[n];
		
		for(int i=0; i<n; i++) {
			arr[i] = sc.nextInt();
		}
		
		int max = 0;
		for(int i=0; i<n; i++) {
			int count_plus = 0;
			for(int j=i; j<n; j++) {
				if(j+1<n && arr[j] >= arr[j+1])count_plus++;
				else break;
			}
			int count_minus = 0;
			for(int j=i; j<n; j++) {
				if(j+1<n && arr[j] <= arr[j+1])count_minus++;
				else break;
			}
			int count = Math.max(count_plus, count_minus);
			if(max < count) max = count;
			
		}
		System.out.println(max+1);
	}
}
