import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SWEA_2007_패턴마디의길이 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine().trim());
		
		for(int tc=1; tc<=t; tc++) {
			
			sb.append("#").append(tc).append(" ");
			String text = br.readLine();
			
			int len = 0;
			for(int i=0; i<text.length(); i++) {
				String word = text.substring(0, 1+i);
				len = word.length();
				
				if(text.substring(1+i, 1+i+len).equals(word)) {
					break;
				}
			}
			
			sb.append(len).append("\n");
		}
		System.out.println(sb.toString());
	}
}
