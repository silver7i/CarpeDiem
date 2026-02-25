import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_4963_섬의개수 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		while(true) {
			st = new StringTokenizer(br.readLine());
			int w = Integer.parseInt(st.nextToken());
			int h = Integer.parseInt(st.nextToken());
			
			if(w == 0 && h == 0) break;
			int[][] map = new int[h][w];
			int[][] isChecked = new int[h][w];
			
			int cnt = 0;
			
			//상, 하, 좌, 우, 좌상단, 우상단, 좌하단, 우하단
			int[] dx = {0, 0, -1, 1, -1, 1, -1, 1};
			int[] dy = {-1, 1, 0, 0, -1, -1, 1, 1};
			
			Queue<Integer> queue = new ArrayDeque<>();
			
			int start_x = -1;
			int start_y = -1;
			for(int i=0; i<h; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<w; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if(map[i][j] == 1 && start_x == -1) {
						start_x = j;
						start_y = i;
						
					}
				}
			}
			
			if(start_x == -1) {
				System.out.println(cnt);
				continue;
			}
			else {
				queue.add(start_x);
				queue.add(start_y);

				while(!queue.isEmpty()) {
					int x = queue.poll();
					int y = queue.poll();
					isChecked[y][x] = 1;
					
					for(int d=0; d<8; d++) {
						int nx = x + dx[d];
						int ny = y + dy[d];
						
						if(nx >= 0 && nx < w && ny >= 0 && ny < h) {
							if(isChecked[ny][nx] == 0 && map[ny][nx] == 1) {
								isChecked[ny][nx] = 1;
								queue.add(nx);
								queue.add(ny);
							}
						}
					}
					
					if(queue.isEmpty()) {
						cnt++;
						for(int i=0; i<h; i++) {
							boolean isFind = false;
							for(int j=0; j<w; j++) {
								if(map[i][j] == 1 && isChecked[i][j] == 0) {
									queue.add(j);
									queue.add(i);
									isFind = true;
									break;
								}
							}
							if(isFind)break;
						}
					}
					
				}
				////

			}

			System.out.println(cnt);
			
		}
	}
}
