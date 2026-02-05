import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class SWEA_1218_괄호짝짓기 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		char[] arr = sc.nextLine().toCharArray();
		Stack<Character> stack = new Stack<>();
		int razer = 0;
		int cnt = 0;
		
		for(int i=0; i<arr.length; i++) {
			if(arr[i] == '(') {
				stack.push(arr[i]);
			}else {
				if(i>=1 && arr[i-1] == '(') {
					razer ++;
					stack.pop();
				}
			}
			
			
		}
		System.out.println(stack.toString());
		System.out.println(razer);
		
	}//main
}