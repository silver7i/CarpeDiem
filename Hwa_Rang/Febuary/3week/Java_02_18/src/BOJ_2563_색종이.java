import java.util.Scanner;

public class BOJ_2563_색종이 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[][] map = new int[100][100];
		
		int n = sc.nextInt();
		for(int t=0; t<n; t++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			
			for(int i=y; i<y+10; i++) {
				for(int j=x; j<x+10; j++) {
					if(map[i][j] == 1) continue;
					map[i][j] = 1;
				}
			}
		}
		
		int sum = 0;
		for(int i=0; i<100; i++) {
			for(int j=0; j<100; j++) {
				if(map[i][j] == 1) sum += 1;
			}
		}
		
		System.out.println(sum);
	}
}
