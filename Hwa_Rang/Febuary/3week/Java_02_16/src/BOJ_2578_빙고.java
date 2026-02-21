import java.util.Scanner;

public class BOJ_2578_빙고 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] map = new int[5][5];
		for(int i=0; i<5; i++) {
			for(int j=0; j<5; j++) {
				map[i][j] = sc.nextInt();
			}
		}
		
		boolean isThree = false;
		int round = 0;
		while(!isThree) {
			round++;
			int n = sc.nextInt();
			for(int i=0; i<5; i++) {
				for(int j=0; j<5; j++) {
					if(map[i][j] == n) {
						map[i][j] = 0;
						break;
					}
				}
			}
			
			if(round >= 12) {
				int cnt = 0;
				// 가로, 세로 검사
				for(int i=0; i<5; i++) {
					int cnt_row = 0;
					int cnt_col = 0;
					for(int j=0; j<5; j++) {
						if(map[i][j] == 0)cnt_row++;
						if(map[j][i] == 0)cnt_col++;
					}
					
					if(cnt_row == 5)cnt++;
					if(cnt_col == 5)cnt++;
				}
				
				if(cnt >= 3) {
					isThree = true;
				}
				
				// 대각선 검사
				int cnt_line1 = 0;
				int cnt_line2=0;
				for(int i=0; i<5; i++) {
					if(map[i][i] == 0)cnt_line1++;
					if(map[i][4-i] == 0)cnt_line2++;

				}
				if(cnt_line1 == 5)cnt++;
				if(cnt_line2 == 5)cnt++;
				
				if(cnt >= 3) isThree = true;
				
			}
		}
		
		System.out.println(round);
		
	}
	
	
}
