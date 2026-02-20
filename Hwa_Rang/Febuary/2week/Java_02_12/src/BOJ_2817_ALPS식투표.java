import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class BOJ_2817_ALPS식투표 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int vote5 = sc.nextInt()/100*5;
		
		int pCount = sc.nextInt();
		
		
		
		Map<String, Integer> people = new HashMap<>();
		
		for(int i=0; i<pCount; i++) {
			people.put(sc.next(), sc.nextInt());
		}
		
		List<String> pSort = new ArrayList<>();
		
		for(String s : people.keySet()) {
			if(people.get(s) >= vote5)
				pSort.add(s);
		}
		
		Collections.sort(pSort);

		
		Map<Integer, String> alps = new HashMap<>();
		
		List<Integer> maxValues = new ArrayList<>();
		
		for(String s : pSort) {
			for(int i=1; i<=14; i++) {
				alps.put(people.get(s) / i, s);
				maxValues.add(people.get(s) / i);
			}
		}
		
		Collections.sort(maxValues);
		
		Map<String, Integer> result = new HashMap<>();
		
		for(String name : pSort) {
			result.put(name, 0);
		}
		
		int idx = maxValues.size()-1;
		
		for(int i=0; i<14; i++) {
			result.put(alps.get(maxValues.get(idx-i)), result.get(alps.get(maxValues.get(idx-i)))+1);
		}
		
		for(String name : result.keySet()) {
			System.out.println(name+" "+result.get(name));
		}
	}
}
