import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SWEA_1288_새로운불면증치료법_bit {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=t; tc++) {
			sb.append("#").append(tc).append(" ");
			
			int N = Integer.parseInt(br.readLine());
			
			//비교군 (10개 비트 1로 채우기)
			int compare = (1 << 10)-1;
			
			int count = 1;
			int bit = 0;
			while(true) {
				//int형을 문자열로 변환 후 문자 배열로 변환 
				char[] arr = String.valueOf(N*count).toCharArray();
				
				for(char c: arr) {
					int n = c - '0'; //각 문자를 다시 숫자로 변환
					
					//비트연산으로 나온 숫자 n만큼 비트를 밀어넣음
					bit = bit | (1 << n);
				}
				
				//일치하면 그만
				if(compare == bit) break;
			
				count++;
			}
			
			sb.append(N*count).append("\n");
		}
		System.out.print(sb);
		
	}
}
