import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class BOJ_1181_단어정렬 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		Set<String> set = new HashSet<>();
		int n = sc.nextInt();
		
		for(int i=0; i<n; i++) {
			set.add(sc.next());
		}
		
		//인덱스 0을 하면 배열길이 자동조절
		String[] arr = set.toArray(new String[0]);
		
		Arrays.sort(arr);
		
		boolean isChanged = false;

		
		while(!isChanged) {
			int checked = 0;
			for(int i=0; i<arr.length-1; i++) {
				if(arr[i].length() > arr[i+1].length()) {
					String tmp = new String();
					tmp = arr[i+1];
					arr[i+1] = arr[i];
					arr[i] = tmp;
					checked++;
				}
			}
			if(checked==0)isChanged = true;
		}
		

		for(int i=0; i<arr.length; i++) {
			System.out.println(arr[i]);
		}
		
		
	}
}
