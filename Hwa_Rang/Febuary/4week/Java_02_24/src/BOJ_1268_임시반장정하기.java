import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class BOJ_1268_임시반장정하기 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		int[][] arr = new int [6][n+1];
		Set<Integer>[] student = new Set[n+1];
		
		for(int i=1; i<=n; i++) {
			student[i] = new HashSet<>();
		}
		
		for(int i=1; i<=n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j=1; j<=5; j++) {
				arr[j][i] = Integer.parseInt(st.nextToken());
			}
		}

		
		for(int i=1; i<=5; i++) {
			for(int j=1; j<=n; j++) {
				
				for(int k=1; k<=n; k++) {
					if(j==k) continue;
					
					if(arr[i][j] == arr[i][k]) {
						student[j].add(k);
					}
				}
			}
			
		}

		int max = 0;
		int idx = 1;
		for(int i=1; i<n+1; i++) {
			if(max < student[i].size()) {
				max = student[i].size();
				idx = i;
			}
		}
		
		
		System.out.println(idx);
	}
}
