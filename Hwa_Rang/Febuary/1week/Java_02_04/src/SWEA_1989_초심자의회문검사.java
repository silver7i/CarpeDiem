import java.util.Scanner;

public class SWEA_1989_초심자의회문검사 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();

		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			String s = sc.next();
			char[] c = new char[s.length()];
			int result = 1;
			
			for(int i=0; i<s.length(); i++) {
				c[s.length()-1-i] = s.charAt(i);
			}
			
			for(int i=0; i<s.length(); i++) {
				if(!(s.charAt(i) == c[i])) {
					result = 0;
					break;
				}
			}
			
			System.out.println("#"+tc+" "+result);
			
			
			
		}//tc
	}

}
