import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_7569_토마토 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		int h = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[n*h][m]; 
		
		for(int i=0; i<n*h; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 상하좌우 윗층 아랫층
		int[] dr = {-1, 1, 0, 0, -n, n};
		int[] dc = {0, 0, -1, 1, 0, 0};
		
		//매번 카피 뜨는 경우
		//
		//답은 맞았으나 시간 초과 코드
		int cnt = 0;
		boolean isZero = false;
		boolean fullTomato = false;
		
		while(!fullTomato) {
			int[][] copiedMap = new int[n*h][];
			
			for(int i=0; i<n*h; i++) {
				copiedMap[i] = Arrays.copyOf(map[i], m);
			}
			
			for(int i=0; i<n*h; i++) {
				for(int j=0; j<m; j++) {
					if(map[i][j] == 1 && copiedMap[i][j] == 1) {
						
						for(int d=0; d<6; d++) {
							int nr = i+dr[d];
							int nc = j+dc[d];
							
							if(nr >= n*(i/n) && nc >= 0 && nr < n + n*(i/n) && nc < m && d<4) {
								if(!(map[nr][nc] == -1) && map[nr][nc] == 0) {
									map[nr][nc] = 1;
//									System.out.println(Arrays.toString(map[nr])+" "+nr+" "+nc+"#"+cnt+" "+i+" "+j);
								}
							}else if(nr >= 0 && nc >= 0 && nr < n*h && nc < m && d >=4) {
								if(!(map[nr][nc] == -1) && map[nr][nc] == 0) {
									map[nr][nc] = 1;
//									System.out.println(Arrays.toString(map[nr])+" "+nr+" "+nc+"#"+cnt);
								}
							}
							
						}
					}
				}
			}
			
			
			if(Arrays.deepEquals(map, copiedMap)) {
				for(int i=0; i<n*h; i++) {
					for(int j=0; j<m; j++) {
						if(map[i][j] == 0) {
							System.out.println(-1);
							isZero = true;
							break;
						}
					}
					if(isZero) break;
				}
				
				if(!isZero) {
					fullTomato = true;
					System.out.println(cnt);
				}else {
					break;
				}
				
			}
			
			cnt++;
		}
		
	}
}
