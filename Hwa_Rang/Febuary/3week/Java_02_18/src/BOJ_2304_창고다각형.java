import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class BOJ_2304_창고다각형 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		Map<Integer, Integer> map = new TreeMap<>();
		
		for(int i=0; i<n; i++) {
			map.put(sc.nextInt(), sc.nextInt());
		}
		
		Integer[] L = map.keySet().toArray(new Integer[0]);
		int[] H = new int[n];
		
		int max = 0;
		int idx = 0;
		for(int i=0; i<n; i++) {
			H[i] = map.get(L[i]);
			if(max < H[i]) {
				max = H[i];
				idx = i;
			} 
		}
		
		int sum = 0;
		for(int i=0; i<=idx; i++) {
			for(int j=i+1; j<=idx; j++) {
				if(H[i] < H[j]) {
					sum += H[i] * (L[j] - L[i]);
					i = j-1;
					break;
				}
				
				else {
					continue;
				}
			}  
		}
		
		System.out.println(sum);
		
		int n_max = H[n-1];
		List<Integer> n_idx = new ArrayList<>(); 
		for(int i=n-1; i>idx; i--) {
			if(n_max < H[i]) {
				n_idx.add(i);
			}
		}
		
		if(n_max == H[n-1]) {
			sum += H[idx];
			System.out.println(sum);
			sum += H[n-1]*(L[n-1] - L[idx]);
		}
		else {
			sum += H[idx];
			for(int i=n_idx.size()-1; i>=0; i++) {
				
			}
		}
		
		System.out.println(Arrays.toString(L));
		System.out.println(Arrays.toString(H));
		System.out.println(sum);
		
		
		
		
	}
}
