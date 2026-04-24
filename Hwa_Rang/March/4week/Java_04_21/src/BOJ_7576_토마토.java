import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_7576_토마토 {
	
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static int m, n;
	static int[][] map, visited;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		
		List<Integer> tomato = new ArrayList<>();
		
		map = new int[n][m];
		visited = new int[n][m];
		boolean fullTomato = true;
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				
				if(map[i][j] == 1) {
					tomato.add(i);
					tomato.add(j);
				}
				
				else if(map[i][j] == 0) {
					fullTomato = false;
				}
			}
		}
		
		bfs(tomato);
		
		if(fullTomato)System.out.println(0);
		else {
			int max = 0;
			boolean NoTomato = false;
			for(int i=0; i<n; i++) {
				for(int j=0; j<m; j++) {
					if(map[i][j] == 0) {
						NoTomato = true;
						break;
					}
					if(max < visited[i][j]) max = visited[i][j];
				}
				if(NoTomato) break;
			}
			if(NoTomato)System.out.println(-1);
			else System.out.println(max-1);
		}
		
		
	}
	
	static void bfs(List<Integer> list) {
		Queue<Integer> q = new ArrayDeque<>();
		for(int i=0; i<list.size(); i+=2) {
			int y = list.get(i);
			int x = list.get(i+1);
			
			visited[y][x] = 1;
			q.add(y);
			q.add(x);
		}
		
		while(!q.isEmpty()) {
			int y = q.poll();
			int x = q.poll();
			
			for(int d=0; d<4; d++) {
				int ny = y+dy[d];
				int nx = x+dx[d];
				
				if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
				
				if(map[ny][nx] == 0 && visited[ny][nx] == 0) {
					q.add(ny);
					q.add(nx);
					visited[ny][nx] = visited[y][x] + 1;
					map[ny][nx] = 1;
				}
			}
		}
	}
}
