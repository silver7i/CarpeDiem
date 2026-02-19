import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ_17298_오큰수 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int [] arr = new int [n];
		int [] printer = new int [n];
		Stack<Integer> stack = new Stack<>();
		
		
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			printer[i] = -1;
		}
		
		for(int i=0; i<n; i++) {
			while(true) {
				if(!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
					printer[stack.pop()] = arr[i];
				}
				else break;
			}
			
			stack.add(i);
			
		}
		
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(printer[i]).append(" ");
        }

        System.out.println(sb);
		
	}
}
