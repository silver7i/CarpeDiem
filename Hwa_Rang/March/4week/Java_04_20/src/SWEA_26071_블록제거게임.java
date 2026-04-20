import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class SWEA_26071_블록제거게임 {
	
	static int max;
	static int n;
	static List<Integer> map;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st; 
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append(" ");
			n = Integer.parseInt(br.readLine());
			map = new ArrayList<>();
			
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<n; i++) {
				map.add(Integer.parseInt(st.nextToken()));
			}
			
			max = 0;
			dfs(0);
			
			sb.append(max).append("\n");
			
		}
		System.out.println(sb);
	}
	static void dfs(int sum) {
		if(map.size() == 0) {
			if(max < sum) max = sum;
			return;
		}
		
		for(int i=0; i<map.size(); i++) {
			int tmp = map.get(i);
			if(i == 0 && map.size() > 1) {
				map.remove(i);
				dfs(sum + map.get(i));
				map.add(i, tmp);
			}
			else if(i == map.size()-1 && map.size()>1) {
				map.remove(i);
				dfs(sum + map.get(i-1));
				map.add(i, tmp);
			}
			else if(map.size() == 1) {
				map.remove(i);
				dfs(sum + tmp);
				map.add(tmp);
			}
			
			else {
				map.remove(i);
				dfs(sum + (map.get(i-1) * map.get(i)));
				map.add(i, tmp);
			}
		}
	}
}
