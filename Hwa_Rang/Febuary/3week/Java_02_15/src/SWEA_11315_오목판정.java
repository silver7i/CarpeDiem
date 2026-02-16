import java.util.Arrays;
import java.util.Scanner;

public class SWEA_11315_오목판정{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = Integer.parseInt(sc.nextLine());
		for (int tc = 1; tc <= t; tc++) {

			int n = Integer.parseInt(sc.nextLine());

			char[][] map = new char[n][n];

			for (int i = 0; i < n; i++) {
				map[i] = sc.nextLine().toCharArray();
			}
			
			
//			for(char[] c: map) {
//				System.out.println(Arrays.toString(c));
//			}
			
			boolean isFind = false;
			
			int[] dr = {0, 1, 1, 1};
			int[] dc = {1, 0, 1, -1};
			
			for(int i=0;i<n;i++){
			    for(int j=0;j<n;j++){
			        if(map[i][j]=='o'){
			            for(int d=0; d<4; d++){
			                int cnt = 1;
			
			                for(int k=1;k<5;k++){
			                    int nr = i + dr[d]*k;
			                    int nc = j + dc[d]*k;
			
			                    if(nr<0 || nc<0 || nr>=n || nc>=n) break;
			                    if(map[nr][nc]=='o') cnt++;
			                    else break;
			                }
			
			                if(cnt==5){
			                    isFind = true;
			                    break;
			                }
			            }
			        }
			    }
			}

			
			if(isFind) System.out.println("#" + tc + " " + "YES");
			else System.out.println("#" + tc + " " + "NO");
			
		}
	}
}
