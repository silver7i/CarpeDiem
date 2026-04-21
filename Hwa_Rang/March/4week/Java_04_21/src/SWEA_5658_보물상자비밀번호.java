import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class SWEA_5658_보물상자비밀번호 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append(" ");
			
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());
			
			StringBuilder nsb = new StringBuilder();
			
			nsb.append(br.readLine());
			
			Set<String> code = new TreeSet<>();

			int len = n/4;
			
			for(int i=0; i<n; i++) {
				nsb.append(nsb.charAt(0));
				nsb.deleteCharAt(0);
				
				for(int j=0; j<n; j+=len) {
					String text = nsb.substring(j, j+len);
					code.add(text);
				}
			}
			
			int cnt = 0;
			int sum = 0;
			String[] nCode = code.toArray(new String[code.size()]);
			
			
			for(int i=nCode.length-1; i>=0; i--) {
				cnt++;
				if(cnt == k) {
					
					for(int j=0; j<len; j++) {
						if(nCode[i].charAt(j) - '0' >= 10) {
							int tmp = nCode[i].charAt(j)-'A'+10;
							sum += (tmp*Math.pow(16, len-1-j));
						}
						else {
							int tmp = nCode[i].charAt(j)-'0';
							sum += (tmp*Math.pow(16, len-1-j));
						}
					}
				}
			}
			
			sb.append(sum).append("\n");
		}
		System.out.println(sb);
		
	}
}
