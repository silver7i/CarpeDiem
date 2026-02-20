import java.util.Arrays;
import java.util.Scanner;

public class BOJ_10157_자리배정 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int c = sc.nextInt();
		int r = sc.nextInt();
		
		int n = sc.nextInt();
		
		int[][] map = new int[r+1][c+1];
		
		int i = 1;
		int j = 1;
		int count = 1;
		int d = 0;
		
		
		while(count < r*c) {
			//상
			if(d == 0) { 
				while(i < r && map[i+1][j] == 0) {
					map[i++][j] = count++;
				}
				d = 1;
			}
			
			//우
			if(d == 1) {
				while(j < c && map[i][j+1] == 0) {
					map[i][j++] = count++;
				}
				d=2;
			}
			
			//하
			if(d==2) {
				while(i > 1 && map[i-1][j] == 0) {
					map[i--][j] = count++;
				}
				d=3;
			}
			
			//좌
			if(d==3) {
				while(j> 1 && map[i][j-1] == 0) {
					map[i][j--] = count++;
				}
				d=0;
			}
			
		}
		
		map[i][j] = count;
		
		if(n > r*c) {
			System.out.println(0);
		}
		else {
			for(int y=1; y<=r; y++) {
				for(int x=1; x<=c; x++) {
					if(map[y][x] == n) {
						System.out.println(x+" "+y);
					}
				}
			}
		}
		
		
		
	}
}
