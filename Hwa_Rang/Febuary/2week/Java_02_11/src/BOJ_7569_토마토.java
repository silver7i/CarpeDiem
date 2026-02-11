import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_7569_토마토 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		int h = Integer.parseInt(st.nextToken());
		
		int[][][] map = new int[h][n][m];
		int[][][] visited = new int[h][n][m];
		
		//bfs를 위한 큐 생성
		Queue<Integer> queue = new ArrayDeque<>();
		
		for(int i=0; i<h; i++) {
			for(int j=0; j<n; j++) {
				st = new StringTokenizer(br.readLine());
				for(int k=0; k<m; k++) {
					map[i][j][k] = Integer.parseInt(st.nextToken());
					if(map[i][j][k] == 1) {
						queue.add(i);
						queue.add(j);
						queue.add(k);
						visited[i][j][k] = 1;
					}
				}
			}
		}
		
		// 윗층 아랫층 상하좌우
		int[] dh = {-1, 1, 0, 0, 0, 0};
		int[] dr = {0, 0, -1, 1, 0, 0};
		int[] dc = {0, 0, 0, 0, -1, 1};	

		
		while(!queue.isEmpty()) {
			
				int z = queue.poll();
				int y = queue.poll();
				int x = queue.poll();
				
				if(z-1 >= 0) {
					if(map[z-1][y][x] == 0 && visited[z-1][y][x] == 0) {
						visited[z-1][y][x] = visited[z][y][x] + 1;
						map[z-1][y][x] = 1;
						
						queue.add(z-1);
						queue.add(y);
						queue.add(x);


					}
				}
				
				
				if(z+1 < h) {
					if(map[z+1][y][x] == 0 && visited[z+1][y][x] == 0) {
						visited[z+1][y][x] = visited[z][y][x] + 1;
						map[z+1][y][x] = 1;
						
						queue.add(z+1);
						queue.add(y);
						queue.add(x);
						
					}
				}
				
				if(y-1 >= 0) {
					if(map[z][y-1][x] == 0 && visited[z][y-1][x] == 0) {
						visited[z][y-1][x] = visited[z][y][x] + 1;
						map[z][y-1][x] = 1;
						
						queue.add(z);
						queue.add(y-1);
						queue.add(x);

					}
				}
				
				if(y+1 < n) {
					if(map[z][y+1][x] == 0 && visited[z][y+1][x] == 0) {
						visited[z][y+1][x] = visited[z][y][x] + 1;
						map[z][y+1][x] = 1;
						
						queue.add(z);
						queue.add(y+1);
						queue.add(x);

					}
				}
				
				
				if(x-1 >= 0) {
					if(map[z][y][x-1] == 0 && visited[z][y][x-1] == 0) {
						visited[z][y][x-1] = visited[z][y][x] + 1;
						map[z][y][x-1] = 1;
						
						queue.add(z);
						queue.add(y);
						queue.add(x-1);

					}
				}
				
				if(x+1 < m) {
					if(map[z][y][x+1] == 0 && visited[z][y][x+1] == 0) {
						visited[z][y][x+1] = visited[z][y][x] + 1;
						map[z][y][x+1] = 1;
						
						queue.add(z);
						queue.add(y);
						queue.add(x+1);

					}
				}	
			
		}
		
		boolean isZero = false;
		int max = 0;
		for(int i=0; i<h; i++) {
			for(int j=0; j<n; j++) {
				for(int k=0; k<m; k++) {
					if(map[i][j][k] == 0) {
						System.out.println(-1);
						isZero = true;
						break;
					}
					
					else if(max < visited[i][j][k])
						max = visited[i][j][k];
				}
				if(isZero) break;
			}
			if(isZero)break;
		}
		
		if(max == 1) {
			System.out.println(0);
		}else if(!isZero){
			//턴 돌기 전부터 1이었던거 제외
			System.out.println(max-1);
		}

		
	}
}
