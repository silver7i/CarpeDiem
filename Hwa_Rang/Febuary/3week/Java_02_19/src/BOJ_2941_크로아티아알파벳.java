import java.util.Scanner;

public class BOJ_2941_크로아티아알파벳 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String[] word = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
		
		String text = sc.next();
		

		int cnt = text.length();
		int len = text.length();
		for(int i=0; i<len; i++) {
			if(i+1<len) {
				if(text.charAt(i) == 'c') {
					if(text.charAt(i+1) == '=' || text.charAt(i+1) == '-') {
						cnt--;
						i++;
						continue;
					}
				}
				
				else if(text.charAt(i) == 'd' && text.charAt(i+1) == '-') {
					cnt--;
					i++;
					continue;
				}
				
				else if(text.charAt(i) == 'l' && text.charAt(i+1) == 'j') {
					cnt--;
					i++;
					continue;
				}
				
				else if(text.charAt(i) == 'n' && text.charAt(i+1) == 'j') {
					cnt--;
					i++;
					continue;
				}
				
				else if(text.charAt(i) == 's' && text.charAt(i+1) == '=') {
					cnt--;
					i++;
					continue;
				}
				
				else if(text.charAt(i) == 'z' && text.charAt(i+1) == '=') {
					cnt--;
					i++;
					continue;
				}
			}
			if(i+2 < len && text.charAt(i) == 'd' && text.charAt(i+1) == 'z' && text.charAt(i+2) == '=') {
				cnt-=2;
				i+=2;
				continue;
			}

			
		}
		
		System.out.println(cnt);
	}
}
