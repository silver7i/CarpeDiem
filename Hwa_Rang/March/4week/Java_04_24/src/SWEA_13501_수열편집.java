import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Node {
	int val;
	Node next;
	
	public Node(int val, Node next) {
		this.val = val;
		this.next = next;
	}
	
}


public class SWEA_13501_수열편집 {
	
	static final StringBuilder SB = new StringBuilder();
	
	static int N, M, L;
	static Node head;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<=t; tc++) {
			SB.append("#").append(tc).append(" ");
		}
	}
}
