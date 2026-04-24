import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Set;
import java.util.TreeSet;

public class SWEA_1288_새로운불면증치료법_bit {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append(" ");
			
			String s = br.readLine();
			int n = Integer.parseInt(s);
			
			int bit = 1023;
			
			int x=0;
			
			Set<Integer> dict = new TreeSet<>();
			
			for(int i=0; i<s.length(); i++) {
				dict.add(s.charAt(i))
			}
			
			
			while(true) {
				
			}
		}
	}
}
