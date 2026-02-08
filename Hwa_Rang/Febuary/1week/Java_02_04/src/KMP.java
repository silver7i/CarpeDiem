
/*
KMP : 최장 길이의 일치하는 접두사 == 접미사 정보를 이용해 점프
LPS : Longest proper Prefix which is also a Suffix
 - proper: 자기 자신(전체)은 제외
 - ex) "level"
 	- prefix: l, le, lev, leve(o), level(x)
 	- suffix: l, el, vel, evel
 	-> LPS: "l"
 */
import java.util.Arrays;

public class KMP {
	//2단계
	//1. LPS 길이를 구하는 배열(pi)만들기
	//2. LPS 배열을 이용해 점프하여 패턴 찾기 로직 만들기
	
	//패턴안에서 접미사, 접두사 일치하는 최장 길이를 찾아 저장
	public static int[] computeLPS(String P) {
		int m = P.length(); //패턴의 길이
		int[] pi = new int[m]; // 길이만큼 pi배열 생성
		//패턴의 부분 문자에 대해 전부 LPS를 계산한다.
		int j = 0; // j: 현재까지 일치한 접두사의 길이
		for(int i=1; i<m; i++) { //i=0인 경우는 문자열 길이
			while(j>0 && P.charAt(j)!= P.charAt(i)) { //j와 i가 일치하지 않는 경우
				j = pi[j-1]; // 직전까지 매칭 성공했던 길이로 돌아감(처음(0)으로 돌아가는 것이 아님)
		
			}
			
			if(P.charAt(j)==P.charAt(i)){// 접두사 끝 다음과 현재 i의 길이가 일치하다면
				j++; //새로찾은 일치하는 LPS의 끝문자를 포함(일치함)
			}
			
			pi[i] = j;
		}//for
		return pi;
	}//def


public static void kmp(String T, String P) {
		int n = T.length();
		int m = P.length();
		
		if(m == 0) return;
		
		int[] pi = computeLPS(P); //LPS배열 가져오기
		System.out.println("pi: "+Arrays.toString(pi));
		
		int j = 0; // j: 패턴의 문자열 중에서 현재까지 일치한 문자열의 길이
		for(int i=0; i<n; i++) { //원본 문자열 T를 처음부터 끝까지
			
			while(j > 0 && T.charAt(i) != P.charAt(j)) {
				j =pi[j-1]; //직전까지 일치했던 구간에서, 가장 길게
			}
			
			if(T.charAt(i) == P.charAt(j)) {
				j++;
			}
			
			if(j == m) { //패턴문자열길이(j)가 m이 된다면 일치한 것
				System.out.printf("found at: %d\n", i-m+1); // i에서 패턴의 길이(m)만큼 빼주면 
				j = pi[j-1]; // 그 다음 패턴을 찾으러 간다. 그 다음 패턴을 찾으러 갈 때도 lps만큼 점프
			}
			
		}
		
		
	}
	
	public static void main(String[] args) {
		KMP.kmp("aaabaaataaabaaac", "aaabaaac");
	}
	
	
	
	
	
	
	
	
	
}
