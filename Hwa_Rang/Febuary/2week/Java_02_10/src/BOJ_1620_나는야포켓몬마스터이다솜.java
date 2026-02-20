import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class BOJ_1620_나는야포켓몬마스터이다솜 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		Map<String, String> pokemon_s = new HashMap<>();
		Map<String, String> pokemon_n = new HashMap<>();
		
		for(int i=1; i<=n; i++) {
			String name = sc.next();
			pokemon_s.put(name, ""+i);
			pokemon_n.put(""+i, name);
		}
		
		for(int i=0; i<m; i++) {
			String q = sc.next();
			if(pokemon_n.containsKey(q)) {
				System.out.println(pokemon_n.get(q));
			}else {
				System.out.println(pokemon_s.get(q));
			}
		}
	}
}
