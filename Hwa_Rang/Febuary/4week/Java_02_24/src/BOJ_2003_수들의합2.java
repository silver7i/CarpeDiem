import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2003_수들의합2 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] sum = new int[n+1];
		
		st = new StringTokenizer(br.readLine());
		for(int i=1; i<=n; i++) {
			if(i==0) {
				sum[i] = Integer.parseInt(st.nextToken());
				continue;
			}
			else {
				sum[i] = sum[i-1] + Integer.parseInt(st.nextToken());
			}
		}
		int cnt = 0;
		for(int i=1; i<=n; i++) {
			for(int j=i; j<=n; j++) {
				if(sum[j] - sum[i-1] == m) cnt++;
			}
		}
		
		
		System.out.println(cnt);
		
	}
}
