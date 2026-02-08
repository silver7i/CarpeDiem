import java.util.Scanner;

public class SWEA_5432_쇠막대기자르기 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			String str = sc.next();
			
			int cnt =0;
			int pieceCnt =0;
			// cnt: 막대가 쌓인 갯수, pieceCnt: 조각의 갯수
			
			for(int i=0; i<str.length(); i++) {
				char c = str.charAt(i); //i번째 문자를 검색
				if(c == '(') { //여는 괄호라면
					if(i+1<str.length() && str.charAt(i+1) == '(') {  // 막대기의 시작
						cnt++;
					}
					else if(i+1<str.length() && str.charAt(i+1) == ')'){ //레이저의 시작
						pieceCnt += cnt;
					}
				}
				
				else{ //i번째 문자가 닫는 괄호라면?
					if(i-1>=0 && str.charAt(i-1)==')') { // 막대의 끝
						cnt --;
						pieceCnt++;
					}
					
				}
			}
			
			System.out.println("#"+tc+" "+pieceCnt);
		}
	}
}
