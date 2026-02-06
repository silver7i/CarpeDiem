import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

public class SWEA_1222_계산기1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		
		for(int tc=1; tc<=10; tc++) {
			int n = Integer.parseInt(sc.nextLine());
			
			String s = sc.nextLine();
			StringBuilder sb = new StringBuilder();
			
			Stack<Character> stack = new Stack<>();
			
			
			//후위연산으로 바꾸기
			for(int i=0; i<n; i++) {
				//피연산자
				if(s.charAt(i)-'0'> 0) {
					sb.append(s.charAt(i));
					
				//연산자	
				}else {
					
					if(s.charAt(i) == ')') {
						while(!(stack.peek() == '(')) {
							sb.append(stack.pop());
						}
						
						stack.pop();
						
					}else if(s.charAt(i) == '+') {
						if(stack.isEmpty()) {
							stack.push(s.charAt(i));
						}
						
						else if(stack.peek() == '*') {
							sb.append(stack.pop());
							
							if(stack.peek() == s.charAt(i))
								sb.append(stack.pop());
							stack.push(s.charAt(i));
							
						}else if(stack.peek() == '('){
							stack.push(s.charAt(i));
							
						}else {
							sb.append(s.charAt(i));							
						}
						
					}else {
						if(!(stack.isEmpty()) && stack.peek() == s.charAt(i))
							sb.append(stack.pop());
						stack.push(s.charAt(i));
					}
						
					
				}//else
			
			}//for
			
			while(!stack.isEmpty()) {
				sb.append(stack.pop());
			}
			
			
			
			//계산기 작동
			Stack<Integer> szamit = new Stack<>();
			String postfix = sb.toString();
			for(int i=0; i<postfix.length(); i++) {
				//피연산자
				if(postfix.charAt(i)-'0'> 0) {
					szamit.push(postfix.charAt(i)-'0');
				}
				
				//연산자
				else {

					
					if(postfix.charAt(i) == '*') {
						szamit.push(szamit.pop()*szamit.pop());
					}
					else {
						szamit.push(szamit.pop()+szamit.pop());
					}
					
				}
			}
			
			System.out.println("#"+tc+" "+szamit.pop());
		}
		
	}//main
	
	
	

}
