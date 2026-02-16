import java.util.Scanner;

public class BOJ_2669_직사각형네개의합집합 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int [][] map = new int [100][100];
		
		int sum = 0;
		
		for(int t=0; t<4; t++) {
			int s_x = sc.nextInt();
			int s_y = sc.nextInt();
			int f_x = sc.nextInt();
			int f_y = sc.nextInt();
			
			for(int i=s_y; i<f_y; i++) {
				for(int j=s_x; j<f_x; j++) {
					if(map[i][j] == 1) continue;
					else {
						map[i][j] = 1;
						sum ++;
					}
				}
			}
			
		}
		
		System.out.println(sum);
	}
}
