import java.util.Scanner;

public class SWEA_2001_파리퇴치 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
		
			int n = sc.nextInt();
			int m = sc.nextInt();
			int[][] map = new int[n][n];
			
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					map[i][j] = sc.nextInt();
				}
			}//map
			
			int max = 0;
			int cnt = 0;
			

			
			for(int i=0; i<n-m+1; i++) {
				for(int j=0+cnt; j<n-m+1; j++) {
					
					int sum = 0;
					for(int r=0+i; r<m+i; r++) {
						for(int c=0+j; c<m+j; c++) {
							sum += map[r][c];
						}
					}
					if(max < sum) max=sum;
					
				}//j
			}//i
		
			
			
			
			System.out.println("#"+tc+" "+max);
		}//테스트케이스
	}//메인

}
