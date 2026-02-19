import java.util.Scanner;

public class SWEA_1213_String {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		
		for(int tc=1; tc<=10; tc++) {
			int t = sc.nextInt();
			
			String word = sc.next();
			//앞뒤에 word가 있느경우
			String s = "가"+sc.next()+"나";
			int result = s.split(word).length-1;
			
			System.out.println("#"+t+" "+result);
		}
	}

}
