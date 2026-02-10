import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BOJ_28278_스택2 {
	public static void main(String[] args) throws IOException {
		Stack<String> stack = new Stack<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		int n = Integer.parseInt(br.readLine());
		for(int i=0; i<n; i++) {
			String[] num = br.readLine().split(" ");
			switch (num[0]) {
			case "1":
				stack.push(num[1]);
				break;
			case "2":
				if(stack.empty()) {
					System.out.println(-1);
				}else {
					
					System.out.println(stack.pop());
				}
				break;
			
			case "3":
				System.out.println(stack.size());
				break;
				
			case "4":
				if(stack.empty()) {
					System.out.println(1);
				}else {
					System.out.println(0);
				}
				break;
				
			case "5":
				if(stack.empty()) {
					System.out.println(-1);
				}else {
					System.out.println(stack.peek());
				}
				break;
				

			default:
				break;
			}
		}
	}

}
