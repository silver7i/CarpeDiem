import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class SWEA_26071_블록제거게임 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		for(int tc=1; tc<=t; tc++) {
			int n = sc.nextInt();
			List<Integer> arr = new ArrayList<>();
			
			int sum = 0;
			
			for(int i=0; i<n; i++) {
				arr.add(sc.nextInt());
			}
			
			while(arr.size()>0) {
				int max = 0;
				int idx = 0;
				
				if(arr.size() > 2) {
					for(int i=1; i<arr.size()-1; i++) {
						if(max < arr.get(i-1) * arr.get(i+1)) {
							max = arr.get(i-1) * arr.get(i+1);
							idx = i;
						}
					}
					
					if(arr.size() == 3 && idx == 1) {
						int a = arr.get(1)*3;
						int b = arr.get(1) + Math.max(arr.get(0), arr.get(2))*2;
						if(a>b) {
							if(arr.get(0) > arr.get(2)) {
								sum += arr.get(1);
								arr.remove(2);
								continue;
							}
							else {
								sum += arr.get(1);
								arr.remove(0);
								continue;
							}
						}
					}
					
					sum += max;
					arr.remove(idx);					
				}
				
				if(arr.size()==2) {
					int maxArr = arr.get(0);
					if(maxArr < arr.get(1)) {
						sum += arr.get(1);
						arr.remove(0);
					}
					else {
						sum += arr.get(0);
						arr.remove(1);
					}
					
					sum += arr.get(0);
					arr.remove(0);
					
				}
				
				if(arr.size() == 1) {
					sum += arr.get(0);
					arr.remove(0);
				}
				
			}
			
			System.out.println("#"+tc+" "+sum);
		}
	}
}
