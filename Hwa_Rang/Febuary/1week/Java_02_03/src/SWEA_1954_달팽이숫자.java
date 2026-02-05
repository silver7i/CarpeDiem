import java.util.Scanner;

public class SWEA_1954_달팽이숫자 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t=sc.nextInt();
		
		for(int tc=1; tc<=t; tc++) {
			int n = sc.nextInt();
			
			int[][] map = new int[n][n];
			
			int i=0;
			int j=0;
			int d=0;
			int cnt = 1;
			
			while(cnt <= n*n) {
				// 우로 직진인 경우
				if(d == 0) {
					// 맨처음 n-1까지 직진 혹은 이미 값을 넣은 벽을 만남
					if(j == n-1 || (j<n-1 && map[i][j+1] !=0)) {
						d=1;
						map[i++][j] = cnt++;
					}else {
						map[i][j++] = cnt++;
					}
				//아래로 직진	
				}else if(d == 1) {
					// 맨처음 n-1 까지 직진 혹은 이미 값을 넣은 벽을 만남
					if(i == n-1 || (i<n-1 && map[i+1][j] != 0)) {
						d=2;
						//다음방향으로 회전
						map[i][j--] = cnt++;
					}else {
						map[i++][j] = cnt++;
					}
				}else if(d==2) {
					// 맨처음 0 까지 직진 혹은 이미 값을 넣은 벽을 만남
					if(j==0 || (j>0 && map[i][j-1] != 0)) {
						d=3;
						//다음방향으로 회전
						map[i--][j] = cnt++;
					}else {
						map[i][j--] = cnt++;
					}
				}else if(d==3) {
					if(i==0 || (i>0 && map[i-1][j] != 0)) {
						d=0;
						map[i][j++]=cnt++;
					}else {
						map[i--][j] = cnt++;
					}
				}
				
			}
			
		
			System.out.println("#"+tc);
			for(int r=0; r<n; r++) {
				for(int c=0; c<n; c++) {
					System.out.print(map[r][c]+" ");
				}
				System.out.println();
			}
			
		}//tc
	}
}


/// 놓친 포인트
//1. while문 조건 2차원 배열 순회 이므로 n*n
//2. 방향전환 어캐할지 생각
//3. true로 조건이 힘들면 false조건이 좋을 수 있다ㅓ.
