import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_10726_이진수표현_bit {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append(" ");
			
			st = new StringTokenizer(br.readLine());
			
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			//1을 특정 비트만큼 밀고 -1하면 1로 채워넣음
			int bit = (1 << N)-1;
			
			//비트를 and 연산해서 일치하면 ON 아닌 경우 OFF
			if((bit & M) == bit) sb.append("ON");
			else sb.append("OFF");
			
			sb.append("\n");
		}
		
		System.out.print(sb);
	}
}
