import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_5656_벽돌깨기 {
	static int[][] map;
	static int n, w, h, max;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=t; tc++) {
			st = new StringTokenizer(br.readLine());
			
			n =  Integer.parseInt(st.nextToken());
			w =  Integer.parseInt(st.nextToken());
			h =  Integer.parseInt(st.nextToken());
			
			map = new int[h][w];
			
			int sum = 0;
			max = 0;
			for(int i=0; i<h; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<w; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					sum += map[i][j];
				}
			}
			
			dfs(0, sum);
		}
	}
	
	static void dfs(int cnt, int sum) {
		if(cnt == n) {
			if(max < sum) max = sum;
			return;
		}
		
		for(int i=0; i<w; i++) {
			
		}
	}
	
	static void bfs(int y, int x) {
		
	}

}
