import java.util.Scanner;

public class SWEA_1288_새로운불면증치료법 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			int[] count = new int [10];
			
			int n = sc.nextInt();
			
			int cnt = 0;
			while(true) {
				cnt ++;
				int new_num = n*cnt;
				String word = ""+new_num;
				
				for(int i=0; i<word.length(); i++) {
					int number = word.charAt(i)-48;
					count[number]++;
				}
				
				
				boolean isFull = true;
				
				for(int i=0; i<10; i++) {
					if(count[i] == 0) {
						isFull = false;
						break;
					}
				}
				
				if(isFull) break;
				
			}
			
			System.out.println("#"+tc+" "+cnt*n);
			
		}
	}
}
