import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class BOJ_2309_일곱난쟁이 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		List<Integer> arr = new ArrayList<>();
		
		int sum = 0;
		for(int i=0; i<9; i++) {
			arr.add(sc.nextInt());
			sum += arr.get(i);
		}
		
		sum -= 100;
		Collections.sort(arr);
		
		for(int i=0; i<9; i++) {
			for(int j=i; j<9; j++) {
				if(arr.get(i)+arr.get(j)== sum) {
					arr.remove(j);
					arr.remove(i);
					break;
				}
			}
			if(arr.size() == 7) break;
		}
		
		for(int i : arr) {
			System.out.println(i);
		}
	}
}
