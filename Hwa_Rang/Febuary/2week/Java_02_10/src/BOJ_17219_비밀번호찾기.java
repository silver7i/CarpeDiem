import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ_17219_비밀번호찾기 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		Map<String, String> password = new HashMap<>();
		
		
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			password.put(st.nextToken(), st.nextToken());
		}
		
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			System.out.println(password.get(st.nextToken()));
		}
	}
}
