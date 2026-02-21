import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class BOJ_1235_학생번호 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		String[] arr = new String[n];
		
		for(int i=0; i<n; i++) {
			arr[i] = br.readLine();
		}
		
		int idx = 0;
		
		int len = arr[0].length();
		
		for(int i=len-1; i>=0; i--) {
			
			boolean isFind = true;
			List<String> num = new ArrayList<>();
			for(int j=0; j<n; j++) {
				StringBuilder sb = new StringBuilder();
				if(j==0) {
					for(int k=i; k<len; k++) {
						sb.append(arr[j].charAt(k));
					}
					num.add(sb.toString());
				}
				else {
					for(int k=i; k<len; k++) {
						sb.append(arr[j].charAt(k));
					}
					
					for(int s=0; s<num.size(); s++) {
						if(num.get(s).equals(sb.toString())) {
							isFind = false;
							break;
						}
							
						
					}
					
					if(!isFind) break;
					num.add(sb.toString());
				}
				
			}
			
			if(isFind) {
				idx = len-i;
				break;
			}
		}
		
		System.out.println(idx);
	}
}
