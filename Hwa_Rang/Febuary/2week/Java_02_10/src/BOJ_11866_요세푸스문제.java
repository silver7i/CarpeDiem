import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_11866_요세푸스문제 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		Queue<Integer> queue = new ArrayDeque<>();
		
		for(int i=1; i<=n; i++) {
			queue.add(i);
		}
		
		System.out.print("<");
		int cnt = 0;
		while(queue.size() != 1) {
			int tmp = queue.poll();
			cnt++;
			if(cnt%k == 0) {
				System.out.print(tmp+", ");
			}else {
				queue.add(tmp);
			}
		}
		System.out.println(queue.poll()+">");
	}
}
