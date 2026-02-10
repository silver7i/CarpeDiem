import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class BOJ_1764_듣보잡 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		Set<String> name = new TreeSet<String>();
		Set<String> result = new TreeSet<String>();
		
		for(int i=0; i<n; i++) {
			name.add(sc.next());
		}
		
		int cnt = 0;
		for(int i=0; i<m; i++) {
			String s = sc.next();
			if(name.contains(s)) {
				result.add(s);
				cnt ++;
			}
		}
		
		System.out.println(cnt);
		for(String s : result) {
			System.out.println(s);
		}
	}
}
