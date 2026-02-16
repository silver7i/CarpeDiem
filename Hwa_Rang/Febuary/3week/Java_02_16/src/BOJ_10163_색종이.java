import java.util.Scanner;

public class BOJ_10163_색종이 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[][] map = new int[1001][1001];
		int n = sc.nextInt();
		int[][] idx = new int [n][4];
		
		for(int t=1; t<=n; t++) {
			int s_x = sc.nextInt();
			int s_y = sc.nextInt();
			int f_x = s_x+sc.nextInt();
			int f_y = s_y+sc.nextInt();
			idx[t-1] = new int[] {s_x, s_y, f_x, f_y};
			for(int i=s_y; i<f_y; i++) {
				for(int j=s_x; j<f_x; j++) {
					map[i][j] = t;
				}
			}
		}
		
		for(int t=1; t<=n; t++) {
			int count = 0;
			for(int i=idx[t-1][1]; i<idx[t-1][3]; i++) {
				for(int j=idx[t-1][0]; j<idx[t-1][2]; j++) {
					if(map[i][j] == t) count++;
				}
			}
			
			System.out.println(count);
		}
	}
}
