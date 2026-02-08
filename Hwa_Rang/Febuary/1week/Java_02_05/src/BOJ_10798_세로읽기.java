import java.util.Scanner;

public class BOJ_10798_세로읽기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] sList = new String[5];
		int max = 0;
		for(int i=0; i<5; i++) {
			sList[i] = sc.nextLine();
			if(max <sList[i].length()) max = sList[i].length();
		}
		
		for(int i=0; i<max; i++) {
			for(int j=0; j<5; j++) {
				try {
					System.out.print(sList[j].charAt(i));
				} catch (Exception e) {
					continue;
				}
			}
		}
		
		
	}
}
