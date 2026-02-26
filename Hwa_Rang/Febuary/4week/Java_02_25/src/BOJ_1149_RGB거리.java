import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_1149_RGB거리 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		int[][] rgb = new int[n][3];
		int[][] visited = new int[n][3];
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<3; j++) {
				rgb[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int min = Integer.MAX_VALUE;
		for(int i=0; i<3; i++) {
			int sum = rgb[0][i];
			visited[0][i] = 1;
			
			Queue<Integer> queue = new ArrayDeque<>();
			while(!queue.isEmpty()) {
				
			}
		}
		
		System.out.println(min);
	}
}
