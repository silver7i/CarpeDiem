import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class SWEA_1228_암호문1 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		for(int tc=1; tc<=10; tc++) {
			int n = sc.nextInt();
			
			List<Integer> list = new LinkedList<>();
			
			for(int i=0; i<n; i++) {
				list.add(sc.nextInt());
			}
			
			int k = sc.nextInt();
			
			for(int i=0; i<k; i++) {
				String s = sc.next();
				int start = sc.nextInt();
				int last = sc.nextInt();
				
				for(int j=0; j<last; j++) {
					list.add(start+j, sc.nextInt());
				}
				
				
			}
			int cnt = 0;
			System.out.print("#"+tc+" ");
			for(Integer elem : list) {
				System.out.print(elem+" ");
				cnt++;
				if(cnt == 10) break;
			}
			System.out.println();
		}
	}
	

}	
