import java.util.Scanner;

public class BOJ_1157_단어공부 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for(int i=0; i<100; i++) {
			try {
				String s = sc.nextLine();
				System.out.println(s);
			} catch (Exception e) {
				break;
			}
		}
	}
}
