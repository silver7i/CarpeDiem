import java.util.Scanner;

public class BOJ_14696_딱지놀이 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int r = sc.nextInt();
		for(int t=0; t<r; t++) {
			int[] arrA = new int[5];
			int[] arrB = new int[5];
			
			int a = sc.nextInt();
			for(int i=0; i<a; i++) {
				arrA[sc.nextInt()]++;
			}
			
			int b = sc.nextInt();
			for(int i=0; i<b; i++) {
				arrB[sc.nextInt()]++;
			}
			
			boolean isWinner = false;
			
			for(int i=4; i>0; i--) {
				if(arrA[i] > arrB[i]) {
					System.out.println("A");
					isWinner = true;
					break;
				}else if(arrA[i] < arrB[i]) {
					System.out.println("B");
					isWinner = true;
					break;
				}else continue;
			}
			
			if(!isWinner) System.out.println("D");
		}
	}
}
