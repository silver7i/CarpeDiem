import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_10870_피보나치수5 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		System.out.println(fibonachi(n));
	}
	
	static int fibonachi(int n) {
		if(n<=1) return n;
		
		return fibonachi(n-1) + fibonachi(n-2);
	}
}
