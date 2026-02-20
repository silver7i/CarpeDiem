import java.util.Scanner;

public class SWEA_11315_오목판정 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			int n = sc.nextInt();
			
			String[][] map = new String[n][n];
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					map[i][j] = sc.next();
				}
			}
			
			boolean isFive = false;
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					int cnt = 0;
					if(j==0 && map[i][5] != "o") {
						for(int k=0; k<5; k++) {
							if(map[i][k] != "o") break;
							cnt++;
						}
						if(cnt == 5) {
							isFive = true;
							break;
						}
					}
				}
				
				if(isFive) break;
			}
		}
	}
}
