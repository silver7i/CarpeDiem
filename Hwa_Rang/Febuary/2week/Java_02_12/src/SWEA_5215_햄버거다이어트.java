import java.util.Scanner;

public class SWEA_5215_햄버거다이어트 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			int n = sc.nextInt();
			int limit = sc.nextInt();
			
			int[] score = new int[n];
			int[] cal = new int[n];
			
			for(int i=0; i<n; i++) {
				score[i] = sc.nextInt();
				cal[i] = sc.nextInt();

			}

			
			int max = 0;
			
			for(int i=0; i < (1 << n); i++) {
				int score_sum=0;
				int cal_sum=0;
				for(int j=0; j<n; j++) {
					if((i & (1 << j)) != 0) {
						score_sum += score[j];
						cal_sum += cal[j];
					}
				}
				
				if(cal_sum <= limit) {
					if(max < score_sum)
						max = score_sum;
				}
			}
			
			System.out.println("#"+tc+" "+max);
		}
	}
}
