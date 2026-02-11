import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_7576_토마토 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		
		int[][] tomato = new int[n][m];
		int[][] visited = new int[n][m];
		
		Queue<Integer> queue = new ArrayDeque<>();
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				tomato[i][j] = Integer.parseInt(st.nextToken());
				if(tomato[i][j] == 1) {
					queue.offer(i);
					queue.offer(j);
					visited[i][j] = 1;
				}
			}
		}
		
		int[] dx = {0, 0, -1, 1};
		int[] dy = {-1, 1, 0, 0};
		
		while(!queue.isEmpty()) {
			
			int y = queue.poll();
			int x = queue.poll();
			
			for(int d=0; d<4; d++) {
				int ny = y+dy[d];
				int nx = x+dx[d];
				
				if(ny >= 0 && ny <n && nx >=0 && nx <m) {
					if(tomato[ny][nx] == 0 && visited[ny][nx] == 0) {
						queue.add(ny);
						queue.add(nx);
						
						tomato[ny][nx] = 1;
						visited[ny][nx] = visited[y][x] + 1;

					}
				}
			}
			
		}
		
		int max = 0;
		boolean isZero = false;
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(tomato[i][j] == 0) {
					isZero = true;
					break;
				}
				else if(max < visited[i][j])
					max = visited[i][j];
			}
			if(isZero)break;
		}
		
		if(isZero) {
			System.out.println(-1);
		}else if(max == 1) {
			System.out.println(0);
		}else {
			System.out.println(max - 1);
		}
	}
}
