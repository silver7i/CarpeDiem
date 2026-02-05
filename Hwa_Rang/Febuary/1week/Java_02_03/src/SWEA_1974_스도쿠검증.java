import java.util.Arrays;
import java.util.Scanner;

public class SWEA_1974_스도쿠검증 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int[] test = {1,2,3,4,5,6,7,8,9};
		int[] dr = {-1, -1, -1, 0, 0, 0, 1, 1, 1};
		int[] dc = {-1, 0, 1, -1, 0, 1, -1, 0, 1};
		
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			int result = 1;
			int[][] map = new int[9][9];
			
			for(int i=0; i<9; i++) {
				for(int j=0; j<9; j++) {
					map[i][j] = sc.nextInt();
				}// j
			}// i
			
			
			for(int j=0; j<9; j++) {
				int[] tmp1 = new int[9];
				for(int i=0; i<9; i++) {
					tmp1[i] = map[i][j];
				}//i
				
				int[] tmp2 = Arrays.copyOf(map[j], 9);
				Arrays.sort(tmp1);
				Arrays.sort(tmp2);
				if(Arrays.toString(test).equals(Arrays.toString(tmp1))&& Arrays.toString(test).equals(Arrays.toString(tmp2)))
					continue;
				
				result = 0;
				break;

				
			}//j
			
			for(int i=1; i<9; i+=3) {
				for(int j=1; j<9; j+=3) {
					int[] tmp = new int[9];
					
					for(int k=0; k<9; k++) {
						
						tmp[k] = map[i+dr[k]][j+dc[k]];
					}
					
					Arrays.sort(tmp);
					if(Arrays.toString(test).equals(Arrays.toString(tmp))) {
						continue;
					}else {
						result = 0;
						break;
					}
				}
				if(result == 0) break;
			}
			System.out.println("#"+tc+" "+result);
			
		}// 테스트케이스
	}// main

}
