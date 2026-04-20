import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_31575_벽돌깨기 {
	
	//동남
	static int[] dy = {0, 1};
	static int[] dx = {1, 0};
	
	static boolean isYes = false;
	static int n, m;
	static int[][] map;
	static boolean[][] visited;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		map = new int[m][n];
		visited = new boolean[m][n];
		
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		bfs(0, 0);
		
		
		if(isYes)System.out.println("Yes");
		else System.out.println("No");
	}
	
//	static void dfs(int y, int x) {
//		if(y == m-1 && x == n-1) {
//			isYes = true;
//			return;
//		}
//		
//		for(int d=0; d<2; d++) {
//			int ny = y + dy[d];
//			int nx = x + dx[d];
//			
//			if(ny < 0 || ny >= m || nx < 0 || nx >= n) continue;
//			
//			if(map[ny][nx] == 1 && !visited[ny][nx]) {
//				visited[ny][nx] = true;
//				dfs(ny, nx);
//				visited[ny][nx] = false;
//			}
//		}
//	};
	
	
	static void bfs(int y, int x) {
		visited[y][x] = true;
		
		Queue<Integer> q = new ArrayDeque<>();
		q.add(y);
		q.add(x);
		
		while(!q.isEmpty()) {
			int r = q.poll();
			int c = q.poll();
			
			if(r == m-1 && c == n-1) {
				isYes = true;
				break;
			}
			
			for(int d=0; d<2; d++) {
				int nr = r + dy[d];
				int nc = c + dx[d];
				
				if(nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
				
				if(map[nr][nc] == 1 && !visited[nr][nc]) {
					q.add(nr);
					q.add(nc);
					visited[nr][nc] = true;
					System.out.println(nr+" "+nc);
				}
			}
		}
	}

}
