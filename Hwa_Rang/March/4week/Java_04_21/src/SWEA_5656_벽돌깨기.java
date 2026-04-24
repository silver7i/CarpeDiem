import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class SWEA_5656_벽돌깨기 {
	
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, -1, 1};
	
	static int[][] map;
	static int n, w, h, max;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=t; tc++) {
			st = new StringTokenizer(br.readLine());
			
			n = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());
			
			map = new int[h][w];
			
			for(int i=0; i<h; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<w; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			max = 0;
		}
		
	}
	static void dfs(int depth) {
		if(depth == n) {
			int sum = 0;
			for(int i=0; i<h; i++) {
				for(int j=0; j<w; j++) {
					if(map[i][j] != 0) sum+=map[i][j];
				}
			}
			
			if(max < sum) sum = max;
			return;
		}
		
		for(int i=0; i<w; i++) {
			int[][] tmp = new int[h][w];
			
			for(int j=0; j<h; j++) {
				tmp[j] = Arrays.copyOf(map[j], h);
			}
			
			for(int j=0; j<h; j++) {
				if(map[j][i] != 0) {
					bfs(j, i);
					dfs(depth+1);
					break;
				}
			}
			
			for(int j=0; j<h; j++) {
				map[j] = Arrays.copyOf(tmp[j], h);
			}
		}
	}
	
	static void bfs(int y, int x) {
		Queue<Integer> q = new ArrayDeque<>();
		q.add(y);
		q.add(x);
		
		while(!q.isEmpty()) {
			int r = q.poll();
			int c = q.poll();
			
			for(int d=0; d<4; d++) {
				for(int p=0; p<map[r][c]; p++) {
					int nr = r+dy[d]*(p);
					int nc = c+dx[d]*(p);
					
					if(nr >= h || nr < 0 || nc >= w || nc < 0) continue;
					
					map[nr][nc]
				}
			}
		}
	}
}
