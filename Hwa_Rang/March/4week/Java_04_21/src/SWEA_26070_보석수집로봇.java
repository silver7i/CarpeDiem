import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class SWEA_26070_보석수집로봇 {
	
	static int[][] map, d;
	static int cnt, max;

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append(" ");
			int n = Integer.parseInt(br.readLine());
			
			map = new int[n][n];
			d = new int[11][2];
			map[0][0] = 0;
			map[0][1] = 0;
			
			
			max = 0;
			for(int i=0; i<n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<n; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if(map[i][j] != 0) {
						// y좌표
						d[map[i][j]][0] = i;
						// x좌표
						d[map[i][j]][1] = j;						
					}
					if(max < map[i][j]) max = map[i][j];
				}
			}
			
			char curr = 'R';
			cnt = 0; 
			
			for(int i=0; i<max; i++) {
				if(curr == 'R') {
					// x좌표 y좌표 둘다 목표보다 작음
					if(d[i][1] <= d[i+1][1] && d[i][0] < d[i+1][0]) {
						// y좌표를 위한 방향전환
						cnt++;
						curr = 'D';
					}
					else if(d[i][1] < d[i+1][1] && d[i][0] > d[i+1][0]) {
						// y좌표를 위한 3방향 전환
						cnt+=3;
						curr = 'U';
					}
					else if(d[i][1] > d[i+1][1] && d[i][0] < d[i+1][0]) {
						// x좌표1, y좌표1
						cnt+=2;
						curr = 'L';
					}
					
					else {
						cnt+=3;
						curr = 'U';
					}
				}
				
				else if(curr == 'D') {
					// x좌표 y좌표 둘다 목표보다 작음
					if(d[i][1] < d[i+1][1] && d[i][0] < d[i+1][0]) {
						// y좌표를 위한 방향전환
						cnt+=3;
						curr = 'R';
					}
					else if(d[i][1] < d[i+1][1] && d[i][0] > d[i+1][0]) {
						// y좌표를 위한 3방향 전환
						cnt+=3;
						curr = 'R';
					}
					else if(d[i][1] > d[i+1][1] && d[i][0] < d[i+1][0]) {
						// x좌표1, y좌표1
						cnt++;
						curr = 'L';
					}
					
					else {
						cnt+=2;
						curr = 'U';
					}
				}
				
				else if(curr == 'L') {
					// x좌표 y좌표 둘다 목표보다 작음
					if(d[i][1] < d[i+1][1] && d[i][0] < d[i+1][0]) {
						// y좌표를 위한 방향전환
						cnt+=3;
						curr = 'D';
					}
					else if(d[i][1] < d[i+1][1] && d[i][0] > d[i+1][0]) {
						// y좌표를 위한 3방향 전환
						cnt+=2;
						curr = 'R';
					}
					else if(d[i][1] > d[i+1][1] && d[i][0] < d[i+1][0]) {
						// x좌표1, y좌표1
						cnt+=3;
						curr = 'D';
					}
					
					else {
						cnt++;
						curr = 'U';
					}
				}
				
				// curr == U
				else {
					if(d[i][1] < d[i+1][1] && d[i][0] < d[i+1][0]) {
						// y좌표를 위한 방향전환
						cnt+=2;
						curr = 'D';
					}
					else if(d[i][1] < d[i+1][1] && d[i][0] > d[i+1][0]) {
						// y좌표를 위한 3방향 전환
						cnt++;
						curr = 'R';
					}
					else if(d[i][1] > d[i+1][1] && d[i][0] < d[i+1][0]) {
						// x좌표1, y좌표1
						cnt+=3;
						curr = 'L';
					}
					
					else {
						cnt+=3;
						curr = 'L';
					}
				}

			}
			sb.append(cnt).append("\n");
			
		}
		System.out.println(sb);
	}
	
	
}
