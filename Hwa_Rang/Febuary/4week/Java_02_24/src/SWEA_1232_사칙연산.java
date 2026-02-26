import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SWEA_1232_사칙연산 {
	static String[] arr;
	static int[] left;
	static int[] right;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for(int t=1; t<=10; t++) {
			int n = Integer.parseInt(br.readLine());
			arr = new String[n+1];
			left = new int[n+1];
			right = new int[n+1];
			
			for(int i=0; i<n; i++) {
				String[] word = br.readLine().split(" ");
				int v = Integer.parseInt(word[0]);
				arr[v] = word[1];
				if(word.length == 4) {
					left[v] = Integer.parseInt(word[2]);
					right[v] = Integer.parseInt(word[3]);
				}
			}
			
			System.out.println("#"+t+" "+inorder(1));
			
		}
	}
	
	static int inorder (int v) {

		if(arr[v].equals("+")){
			return inorder(left[v]) + inorder(right[v]);
		}
		else if(arr[v].equals("-")) {
			return inorder(left[v]) - inorder(right[v]);
		}
		else if(arr[v].equals("*")) {
			return inorder(left[v]) * inorder(right[v]);
		}
		else if(arr[v].equals("/")) {
			return inorder(left[v]) / inorder(right[v]);
		}
		else {
			return Integer.parseInt(arr[v]);
		}

	}
}
