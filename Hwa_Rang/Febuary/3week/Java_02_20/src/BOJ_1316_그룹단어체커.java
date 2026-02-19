import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class BOJ_1316_그룹단어체커 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int cnt = 0;
		for(int i=0; i<n; i++) {
			List<Character> wordCheck = new ArrayList<>();
			
			boolean isGroup = true;
			String word = br.readLine();
			for(int j=0; j<word.length(); j++) {
				char c = word.charAt(j);
				if(j == 0) {
					wordCheck.add(c);
					continue;
				} 
				
				if(c == word.charAt(j-1)) {
					continue;
				}
				else {
					for(int k=0; k<wordCheck.size(); k++) {
						if(wordCheck.get(k) == c) {
							isGroup = false;
							break;
						}
					}
					if(isGroup) wordCheck.add(c);
				}
			}
			if(isGroup) cnt++;
		}
		
		System.out.println(cnt);
	}
}
