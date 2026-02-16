import java.util.Scanner;

public class BOJ_13300_방배정 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		int [] arr = new int[12];
		
		for(int i=0; i<n; i++) {
			int s = sc.nextInt();
			int y = sc.nextInt();
			
			//남자
			if(s == 0) {
				arr[y*2-2]++;
			}
			//여자
			else arr[y*2-1]++;
		}
		int sum = 0;
		
		for(int i=0; i<12; i++) {
			if(arr[i] == 0) continue;
			
			if(arr[i] % k != 0) {
				sum += (arr[i]/k)+1;
			}
			else sum += arr[i]/k;
		}
		
		System.out.println(sum);
	}
}
