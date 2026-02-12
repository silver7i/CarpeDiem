import java.util.Arrays;
import java.util.Scanner;

public class SWEA_23795_우주괴물 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			int n = sc.nextInt();
			
			int[][] map = new int[n][n];
			
			int x = 0;
			int y = 0;
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					map[i][j] = sc.nextInt();
					if(map[i][j] == 2) {
						x = j;
						y = i;
					}
				}
			}
			
			char d = 'L';
			int org_x = x;
			int org_y = y;
			
			if(d == 'L') {
				while(x-1>=0 && map[y][x-1] == 0) {
					map[y][x-1] = 3;	
					x = x-1;
				}
				d='R';
				x = org_x;
				y = org_y;
			}
			
			if(d == 'R') {
				while(x+1 < n && map[y][x+1] == 0) {
					map[y][x+1] = 3;	
					x = x+1;
				}
				d='U';
				x = org_x;
				y = org_y;
			}
			
			if(d=='U') {
				while(y-1 >= 0 && map[y-1][x] == 0) {
					map[y-1][x] = 3;	
					y = y-1;
				}
				d='D';
				x = org_x;
				y = org_y;
			}
			
			if(d=='D'){
				while(y+1 < n && map[y+1][x] == 0) {
					map[y+1][x] = 3;	
					y = y+1;
				}	
			}
			
			
			int cnt = 0;
			
			for(int i=0; i<n; i++) {
				for(int j=0; j<n; j++) {
					if(map[i][j] == 0) {
						cnt++;
					}
				}
			}
			
			System.out.println("#"+tc+" "+cnt);
			
		}
	}
}
