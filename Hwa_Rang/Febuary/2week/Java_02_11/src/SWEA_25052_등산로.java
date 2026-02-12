import java.util.HashMap;
import java.util.Map;
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
					int cnt = 1;
					while(true) {
						
						Map<Integer, int[]> plus = new HashMap<>();
						
						for(int d=0; d<4; d++) {
							int nr = y+dr[d];
							int nc = x+dc[d];
							
							if(nr >=0 && nr < n && nc >=0 && nc <n) {
								if(map[y][x] > map[nr][nc]) {	
									plus.put(map[nr][nc], new int[] {nr,nc});
								} 
							}
							
						}
						
						if(!plus.isEmpty()) {
							int min = Integer.MAX_VALUE;
							for(int num : plus.keySet()) {
								if(num < min) min = num;
							}
							
							y = plus.get(min)[0];
							x = plus.get(min)[1];
							cnt ++;
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
