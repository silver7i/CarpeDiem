import java.util.Scanner;

public class SWEA_1209_SUM {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		

		for (int tc = 1; tc <= 10; tc++) {
			
			int t = sc.nextInt();
			int[][] map = new int[100][100];

			int max = 0;
			
			//map만들기
			for (int i = 0; i < 100; i++) {
				for (int j = 0; j < 100; j++) {

					map[i][j] = sc.nextInt();

				} // j
			} // i
			
			//행과 열중에 최대 구하기
			for (int i = 0; i < 100; i++) {
				int r_sum = 0;
				int c_sum = 0;
				for (int j = 0; j < 100; j++) {
					r_sum += map[j][i];
					c_sum += map[i][j];
				} // j
				if (max < Math.max(r_sum, c_sum))
					max = Math.max(r_sum, c_sum);
			} // i
			
			// 대각선 중에 최대 구하기
			int line1 = 0;
			int line2 = 0;
			for (int i = 0; i < 100; i++) {
				line1 += map[i][i];
				line2 += map[i][99 - i];
			}
			
			if (max < Math.max(line1, line2))
				max = Math.max(line1, line2);

			System.out.println("#" + t + " " + max);

		} // tc
	}

}
