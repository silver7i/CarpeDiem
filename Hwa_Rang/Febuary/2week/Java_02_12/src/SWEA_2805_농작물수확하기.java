import java.util.Scanner;

public class SWEA_2805_농작물수확하기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			int n = sc.nextInt();
			
			int[][] map = new int[n][n];
			int sum = 0;
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					map[i][j] = sc.nextInt();
					sum += map[i][j];
				}
			}
			
			for(int i=0; i<n; i++) {
				if(i == (n-1)/2) continue;

				for(int j=0; j<n; j++) {
					if(j == (n-1)/2) continue;
				}
			}
		}
	}
}
