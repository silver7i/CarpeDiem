import java.util.Scanner;

public class BOJ_13458_시험감독 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int[] arr = new int[N];
		for(int i=0; i<N; i++) {
			arr[i] = sc.nextInt();
		}
		
		int B = sc.nextInt();
		int C = sc.nextInt();
		
		long cnt = 0;
		
		for(int i=0; i<N; i++) {
			arr[i] -= B;
			cnt++;
			if(arr[i] > 0) {
				if(arr[i]%C == 0) {
					cnt += (arr[i] / C);
				}else {
					cnt += (arr[i]/C) + 1;
				}
			}
		}
		
		
		System.out.println(cnt);
	}

}
