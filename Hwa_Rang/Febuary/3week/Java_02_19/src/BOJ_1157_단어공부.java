import java.util.Scanner;

public class BOJ_1157_단어공부 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int len = 'Z'-'A'+1;
		
		int[] arr = new int[len]; 
		
		String word = sc.next().toUpperCase();
		for(int i=0; i<word.length(); i++) {
			arr[word.charAt(i)-'A']++;
		}
		
		int max = 0;
		int count = 0;
		int idx = 0;
		for(int i=0; i<len; i++) {
			if(max < arr[i]) {
				max = arr[i];
				idx = i;
				count = 0;
			}
			else if(max == arr[i]) {
				count ++;
			}
		}
		
		if(count != 0)System.out.println("?");
		else {
			System.out.println((char)('A'+idx));
		}
		
		
	}
}
