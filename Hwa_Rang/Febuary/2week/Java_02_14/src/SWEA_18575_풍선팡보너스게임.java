import java.util.Scanner;

public class SWEA_18575_풍선팡보너스게임 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		for(int tc=1; tc<=t; tc++) {
			int n = sc.nextInt();
			
			int[][] map = new int [n][n];
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					map[i][j] = sc.nextInt();
				}
			}
			
			int max = Integer.MIN_VALUE;
			int min = Integer.MAX_VALUE;
			
			for(int i=0; i<n; i++) {
				
				for(int j=0; j<n; j++) {
					
					int idx=0;
					int sum = 0;
					
					while(idx<n) {
						sum += map[i][idx];
						sum += map[idx][j];
						idx++;
					}
					
					sum -= map[i][j];
					
					if(max < sum) max = sum;
					if(min > sum) min = sum;
				}
			}
			
			System.out.println("#"+tc+" "+(max-min));
		}
	}
}
