import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;


class Nation implements Comparable<Nation>{
	int name;
	int gold;
	int silver;
	int bronze;
	
	public Nation(int name, int gold, int silver, int bronze) {
		this.name = name;
		this.gold = gold;
		this.silver = silver;
		this.bronze = bronze;
	}
	
	@Override
	public int compareTo(Nation o) {
		if(this.gold > o.gold)
			return -1;
		else if(this.gold < o.gold) return 1;
		else {
			if(this.silver > o.silver) return -1;
			else if(this.silver < o.silver) return 1;
			else {
				if(this.bronze > o.bronze) return -1;
				else if(this.bronze < o.bronze) return 1;
				else return 0;
			}
		}
	}
//
//	@Override
//	public String toString() {
//		return "Nation [name=" + name + ", gold=" + gold + ", silver=" + silver + ", bronze=" + bronze + "]";
//	}
	
}



public class BOJ_8979_올림픽 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		List<Nation> nation = new ArrayList<>();

		for(int i=0; i<n; i++) {
			nation.add(new Nation(sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt()));
		}
		
		nation.sort(Nation :: compareTo);
		
		Map<Integer, Integer> result = new HashMap<>();
		
		for(int i=0; i<nation.size(); i++) {
			if(i!=0 && nation.get(i).compareTo(nation.get(i-1)) == 0) {
				result.put(nation.get(i).name, result.get(nation.get(i-1).name));				
			}
			else {
				result.put(nation.get(i).name, i+1);
			}
		}
		
		System.out.println(result.get(k));
	}
}














