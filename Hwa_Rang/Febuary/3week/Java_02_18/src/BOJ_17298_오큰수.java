import java.util.Scanner;

public class BOJ_17298_오큰수 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] arr = new int[n];
		
		for(int i=0; i<n; i++) {
			arr[i] = sc.nextInt();
		}
		
		for(int i=0; i<n; i++) {
			boolean isFind = false;
			for(int j=i; j<n; j++) {
				if(arr[i] < arr[j]) {
					System.out.print(arr[j]+" ");
					isFind = true;
					break;
				}
			}
			if(!isFind) System.out.print(-1+" ");
		}
		
		
	}
}
