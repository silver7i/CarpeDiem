import java.util.Arrays;
import java.util.Scanner;

public class BOJ_1015_수열정렬 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] arr = new int[n];
		for(int i=0; i<n; i++) {
			arr[i] = sc.nextInt();
		}
		
		int[] copiedArr = Arrays.copyOf(arr, n);
		
		Arrays.sort(copiedArr);
		
		for(int i=0; i<n; i++) {
			
			for(int j=0; j<n; j++) {
				
				if(arr[i] == copiedArr[j]) {
					
					System.out.print(j+" ");
					
					copiedArr[j] = -1;
					break;
				}
			}
		}
		
		
	}
}
