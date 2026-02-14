import java.util.Scanner;

public class SWEA_1979_어디에단어가들어갈수있을까 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int tc = sc.nextInt();		
		
		for(int testcase = 1; testcase<=tc; testcase++) {
			
			int n = sc.nextInt();
			int k = sc.nextInt();
			
			
			int[][] map = new int[n][n];
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					map[i][j] = sc.nextInt();
				}
			}
			
			int cnt = 0;
			
			if(k == n) {
				
				//가로열 확인
				for(int i=0; i<n; i++) {
					int sum = 0;
					for(int j=0; j<n; j++) {
						if(map[i][j] == 1) sum++;
						else break;
					}
					
					if(sum == k) cnt++;
				}
				
				
				//세로열 확인
				for(int j=0; j<n; j++) {
					int sum = 0;
					for(int i=0; i<n; i++) {
						if(map[i][j] == 1) sum++;
						else break;
					}
					
					if(sum == k) cnt++;
				}
			}
			
			else {
				
				//가로열 확인
				for(int i=0; i<n; i++) {
					for(int j=0; j<n; j++) {
						int sum = 0;
						if(j==0) {
							for(int t=j; t<=k; t++) {
								if(map[i][t] == 1) sum ++;
								else break;
							}
						}
						
						else if(j == n-k) {
							for(int t=j; t<k+j; t++) {
								if(map[i][j-1] == 1 ) {
									break; 
								}
								
								if(map[i][t] == 1) {
									sum++;
								}
								
								else break;
							}
						}
						
						else {
							for(int t=j-1; t<k+j; t++) {
								if(t == j-1 && map[i][t] == 1) break;
								
								if(map[i][t] == 1) {
									sum++;
								}
								else break;
							}
						}
						
						if(sum == k) cnt++;
					}
					
				}
				
				//세로열 확인
				
				for(int i=0; i<n; i++) {
					for(int j=0; j<n; j++) {
						int sum = 0;
						if(j==0) {
							for(int t=j; t<=k; t++) {
								if(map[t][i] == 1) {
									sum ++;
									System.out.println("1");
								}	
								else break;
							}
						}
						
						else if(j == n-k) {
							System.out.println("2");
							for(int t=j; t<k+j; t++) {
								if(map[j-1][i] == 1 ) {
									break; 
								}
								
								if(map[t][i] == 1) {
									sum++;
								}
								
								else break;
							}
						}
						
						else {
							System.out.println("3");
							for(int t=j-1; t<k+j; t++) {
								if(t == j-1 && map[t][i] == 1) break;
								
								if(map[t][i] == 1) {
									sum++;
								}
								else break;
							}
						}
						
						if(sum == k) cnt++;
					}
					
				}
				
				
				
			}
			
			System.out.println("#"+testcase+" "+cnt);
			
			
		}
		
		
	}
}
