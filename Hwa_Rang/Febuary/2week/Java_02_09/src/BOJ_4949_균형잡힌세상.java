import java.util.Scanner;
import java.util.Stack;

public class BOJ_4949_균형잡힌세상 {
	public static void main(String[] args) {
		
		
		
		Scanner sc = new Scanner(System.in);
		while(true) {
			boolean stop = false;
			String s = sc.nextLine();
			if(s.equals("."))
				break;
			char[] c = s.toCharArray();
			
			Stack<Character> stack = new Stack<>();
			
			for(int i=0; i<s.length(); i++) {
				if(c[i] == '(') {
					stack.push(c[i]);
				}
				
				else if(c[i] == '[') {
					stack.push('[');
				}
				
				else if(c[i] == ')') {
					if(!(stack.empty()) && stack.peek() == '(')
						stack.pop();
					else {
						stop = true;
						break;
					}
				}
				
				else if(c[i] == ']') {
					if(!(stack.empty()) && stack.peek() == '[')
						stack.pop();
					else {
						stop = true;
						break;
					}
				}
			}
			
			if(!stop && stack.size() == 0)
				System.out.println("yes");
			else{
				System.out.println("no");				
			}
		}
	}
}
