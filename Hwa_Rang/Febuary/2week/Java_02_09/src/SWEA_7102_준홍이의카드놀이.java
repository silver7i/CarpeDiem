import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class SWEA_7102_준홍이의카드놀이 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		for(int tc=1; tc<=t; tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			
			int[] count = new int[n+m+1];
			
			for(int i=1; i<=n; i++) {
				for(int j=1; j<=m; j++) {
					count[i+j]++;
				}
			}
			
			int max = 0;
			
			Set<Integer> result = new TreeSet<>();
			
			for(int i=2; i<m+n+1; i++) {
				if(max < count[i]) max = count[i];
			}
			
			for(int i=2; i<n+m+1; i++) {
				if(max == count[i]) result.add(i);
			}
			
			System.out.print("#"+tc+" ");
			for(int i:result) {
				System.out.print(i+" ");
			}
			System.out.println();
		}
	}

}
