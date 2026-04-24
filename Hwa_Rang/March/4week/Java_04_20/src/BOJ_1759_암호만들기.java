import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class BOJ_1759_암호만들기 {
	
	static String[] dict;
	static int L, C;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		dict = new String[C];
		st = new StringTokenizer(br.readLine());
		
		for(int i=0; i<C; i++) {
			dict[i] = st.nextToken();
		}
		
		
	}
	
	static void dfs(int depth, int cnt) {
		if(depth == L) {
			System.out.println(sb);
		}
		
		for(int i=0; i<dict.length; i++) {
			if(dict[i].equals("a") || dict[i].equals("e") || dict[i].equals("i") || dict[i].equals("o") ||dict[i].equals("u")) {
				if(cnt <= L-2) {
					sb.append(dict[i]);
					dfs(depth+1, cnt+1);
					sb.deleteCharAt(i);
				}
			}
		}
	}
}
