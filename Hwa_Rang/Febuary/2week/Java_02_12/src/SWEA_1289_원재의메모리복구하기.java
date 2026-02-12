import java.util.Arrays;
import java.util.Scanner;

public class SWEA_1289_원재의메모리복구하기 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			
			String s = sc.next();
			
			char[] arr = new char[s.length()];
			
			for(int i=0; i<s.length(); i++) {
				arr[i] = s.charAt(i);
			}
			
			int idx = s.indexOf("1");
			
			int cnt = 0;
			int len = s.length();
			while(idx < len) {
				
				boolean isSame = true;
				
				if(arr[idx] == '1') {
					cnt ++;
					for(int i=idx+1; i<len; i++) {
						if(arr[i] == '1') {
							arr[i] = '0';
						}else {
							arr[i] = '1';
						}
					}
				}
				
				
				for(int i=0; i<len; i++) {
					if(arr[i] != '0') {
						isSame = false;
						break;
					}
						
				}
				
				if(isSame) {
					break;
				}
				
				idx++;
				
			}
			
			System.out.println("#"+tc+" "+cnt);
		}
		
	}
}
