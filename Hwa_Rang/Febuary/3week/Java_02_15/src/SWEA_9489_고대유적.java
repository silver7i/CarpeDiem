import java.util.Scanner;

public class SWEA_9489_고대유적 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			
			int[][] map = new int[n][m];
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					map[i][j] = sc.nextInt();
				}
			}
			
			int max = 0;
			for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					if(map[i][j] == 1) {
						int sum = map[i][j];
						int x = j;
						while(true) {
							if(x+1 < m && map[i][x+1] == 1) {
								sum += map[i][x+1];
								x++;
							}
							else break;
						}
						
						if(max < sum) max = sum;
						
						sum = map[i][j];
						int y = i;
						while(true) {
							if(y+1 < n && map[y+1][j] == 1) {
								sum += map[y+1][j];
								y++;
							}
							else break;
						}
						
						if(max < sum) max = sum;
					}
				}
			}
			
			System.out.println("#"+tc+" "+max);
		}
	}
}
