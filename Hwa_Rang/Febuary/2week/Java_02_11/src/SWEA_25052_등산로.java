import java.util.Scanner;

public class SWEA_25052_등산로 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			int n = sc.nextInt();
			int[][] map = new int[n][n];
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					map[i][j] = sc.nextInt();
				}
			}
			
			int max = 0;
			
			int[] dr = {-1, 1, 0, 0};
			int[] dc = {0, 0, -1, 1};
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					
					int x = j;
					int y = i;
					int cnt = 0;
					boolean move = false;
					while(true) {
						int min = Integer.MAX_VALUE;
						
						for(int d=0; d<4; d++) {
							int nr = y+dr[d];
							int nc = x+dc[d];
							
							if(nr >=0 && nr < n && nc >=0 && nc <n) {
								if(min > map[nr][nc] && map[y][x] > map[nr][nc]) {
									min = map[y][x];
									x = nc;
									y = nr;
									move = true;
									System.out.println("#"+i+" "+j+"sss"+x+" "+y);
									System.out.println();
								} 
							}
						}
						
						if(move) {
							cnt ++;
							move = false;
						}else {
							if(max < cnt) max = cnt;
							break;
						}
					}
					
				}
			}
			
			System.out.println("#"+tc+" "+max);
		}
	}
}
