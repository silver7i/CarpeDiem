import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BOJ_2635_수이어가기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		if(n == 0) {
			System.out.println(0);
			System.out.println(0);			
		}
		else {
			
			int max = 0;
			List<Integer> result = new ArrayList<>();
			for(int i=n; i>=0; i--) {
				List<Integer> tmp = new ArrayList<>();
				int idx = 0; 
				tmp.add(n);
				tmp.add(i);
				while(true) {
					int m = tmp.get(idx)-tmp.get(++idx);
					if(m >= 0) tmp.add(m);
					else break;
				}
				if(max < tmp.size()) {
					max = tmp.size();
					result = tmp;
				}
			}
			
			System.out.println(max);
			for(int i : result) {
				System.out.print(i+" ");
			}
		}
		
	}
}
