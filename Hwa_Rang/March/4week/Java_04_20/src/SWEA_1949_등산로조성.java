import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class SWEA_1949_등산로조성 {
	
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static boolean[][] visited;
	static int[][] map;
	static int n, k, result;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append(" ");
			
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			
			map = new int[n][n];
			visited = new boolean[n][n];
			List<Integer> maxList = new ArrayList<>();
			
			int max = 0;
			
			for(int i=0; i<n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<n; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if(max < map[i][j]) {
						maxList.clear();
						max = map[i][j];
						maxList.add(i);
						maxList.add(j);
					}
					
					else if(max == map[i][j]) {
						maxList.add(i);
						maxList.add(j);
					}
				}
			}
			
			result = 0;
			
			for(int i=0; i<maxList.size(); i+=2) {
				int y = maxList.get(i);
				int x = maxList.get(i+1);

				dfs(y, x, 1, false);


			}

			
			sb.append(result).append("\n");
			
		}
		System.out.println(sb);
	}
	
	static void dfs(int y, int x, int count, boolean isMinus) {
		visited[y][x] = true;
		result = Math.max(result, count);
		
		for(int d=0; d<4; d++) {
			
			int ny = y+dy[d];
			int nx = x+dx[d];
			
			if(ny < 0 || ny >= n || nx < 0 || nx >= n) {
				continue;
			}
			
			if(map[ny][nx] < map[y][x] && !visited[ny][nx]) dfs(ny, nx, count+1, isMinus);
			
			else if(map[ny][nx] >= map[y][x] && map[ny][nx] - k < map[y][x] && (!isMinus) && !visited[ny][nx]) {
				isMinus = true;
				
				int tmp = map[ny][nx];
				map[ny][nx] = map[y][x]-1;
				
				dfs(ny, nx, count+1, isMinus);
				
				map[ny][nx] = tmp;
				isMinus = false;
			}

		}
		
		visited[y][x] = false;

	}
}
