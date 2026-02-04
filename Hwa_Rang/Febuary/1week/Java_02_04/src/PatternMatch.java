
public class PatternMatch {
	public static void main(String[] args) {
		String t= "CCBBCBAABCCCBABCBCAAAACABBACCCCACAABCBBACACAACABCBCCBAABCABBBCCAABBCBBCACABCAAACACABACBCCBAACBCBCAAC";
		
		String p = "CAACBCBCAABCCBCABACACAAACBACACBBCBBAACCBBBACBAABCCBCBACAACACABBCBAACACCCCABBACAAAACBCBABCCCBAABCBBCC";
		
		int N = t.length();
		int max = 0;
		
		for(int r=0; r<100; r++) {
			for(int c=0; c<r+1; c++) {
				String n_p = p.substring(c, 100-r+c);
				int M = n_p.length();
				
				boolean find=false;
				for(int i=0; i<N-M+1; i++) {
					int cnt = 0;
					for(int j=0; j<M; j++) {
						if(n_p.charAt(j) == t.charAt(j+i))
							cnt++;
					}
					if(cnt == M) {
						find = true;
						if(max < cnt)max=cnt;
						break;
					}
				}// t시작지점을 결정한 for문
				
			}//c for
		}//r for
		
		System.out.println(max);
		
		
	}
}
