import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class SWEA_1225_암호생성기 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		for(int tc=1; tc<=10; tc++) {
			int t = sc.nextInt();
			
			Queue<Integer> queue = new LinkedList<>();
			
			for(int i=0; i<8; i++) {
				queue.add(sc.nextInt());
			}
			
			boolean isZero = false;
			
			while(!isZero) {
				for(int i=1; i<=5; i++) {
					if(queue.peek()-i <= 0) {
						queue.poll();
						queue.offer(0);
						isZero = true;
						break;
					}
					queue.offer(queue.poll()-i);
				}
			}
			
			
			System.out.print("#"+t+" ");
			for(int i=0; i<8; i++) {
				System.out.print(queue.poll()+" ");
			}
			System.out.println();
			
			
			
		}
	}
}
