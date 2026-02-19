import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_27433_팩토리얼2 {
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
		long n = Long.parseLong(br.readLine());
		
		System.out.println(factorial(n));
		
		
		
	}
	
	static long factorial(long n) {
		if(n <= 1) return 1;
		
		return n*factorial(n-1);
	}
}
