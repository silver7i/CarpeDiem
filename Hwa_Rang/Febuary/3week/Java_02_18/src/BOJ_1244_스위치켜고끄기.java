import java.util.Scanner;

public class BOJ_1244_스위치켜고끄기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int switchCount = sc.nextInt();
		int[] switchArr = new int[switchCount+1];
		
		for(int i=1; i<=switchCount; i++) {
			switchArr[i] = sc.nextInt();
		}
		
		int n = sc.nextInt();
		for(int i=0; i<n; i++) {
			int s = sc.nextInt();
			int num = sc.nextInt();
			
			if(s == 1) {
				for(int j=1; j<=switchCount; j++) {
					if(j%num == 0) {
						if(switchArr[j] == 1) {
							switchArr[j] = 0;
						}
						else {
							switchArr[j] = 1;
						}
					}
				}
			}
			
			else {
				int idx_s = 0;
				int idx_f = 0;
				for(int j=1; j<num; j++) {
					if(num == 1) {
						break;
					}
					
					if(num-j >= 1 && num+j <= switchCount) {
						int left = num-j;
						int right = num+j;
						if(switchArr[left] == switchArr[right]) {
							idx_s = left;
							idx_f = right;
						}
						else {
							break;
						}
					}
				}
				
				
				if(idx_s == 0) {
					if(switchArr[num] == 1) switchArr[num] = 0;
					else switchArr[num] = 1;
				}
				else {
					for(int j=idx_s; j<=idx_f; j++) {
						if(switchArr[j] == 1) switchArr[j] = 0;
						else switchArr[j] = 1;
					}
				}
				
			}
		}
		
		for(int i=1; i<=switchCount; i++) {
			if(i!= 1 && i%20 == 1)System.out.println();
			System.out.print(switchArr[i]+" ");
		}
	}
}
