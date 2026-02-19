import java.util.Stack;

public class Stack_중위에서후위로 {
	public static void main(String[] args) {
		Stack<Character> stack = new Stack<>();
		String s = "(6+5*(2-8)/2)";
		for(int t=0; t<s.length(); t++) {
			if(s.charAt(t) == '(') {
				stack.push(s.charAt(t));
			}
			else if(s.charAt(t) == '+') {
//				if(stack.peek() == '*' || stack.peek() == '/')
//					stack.pop();
				stack.push(s.charAt(t));
			}
			else if(s.charAt(t) == '-') {
//				if(stack.peek() == '*' || stack.peek() == '/')
//					stack.pop();
				stack.push(s.charAt(t));
			}
			else if(s.charAt(t) == '*') {
				stack.push(s.charAt(t));
			}
			else if(s.charAt(t) == '/') {
				
				stack.push(s.charAt(t));
			}
			else if(s.charAt(t) == ')') {
				while(stack.peek() != '(') {
					System.out.print(stack.pop());
				}
				//마지막 여는 괄호 꺼내기
				stack.pop();
			}else {
				System.out.print(s.charAt(t));
			}
		}
	}
}
