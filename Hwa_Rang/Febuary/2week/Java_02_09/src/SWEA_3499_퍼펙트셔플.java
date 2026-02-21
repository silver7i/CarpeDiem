import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class SWEA_3499_퍼펙트셔플 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int tc=1; tc<=t; tc++) {
			
			int n = sc.nextInt();
			
			Queue<String> q1 = new LinkedList<>();
			Queue<String> q2 = new LinkedList<>();
			
			for(int i=0; i<n; i++) {
				//짝수일때
				if(n%2 == 0) {
					if(i<n/2) {
						q1.offer(sc.next());
					}else {
						q2.offer(sc.next());
					}
				//홀수일때
				}else {
					if(i<n/2+1) {
						q1.offer(sc.next());
					}else {
						q2.offer(sc.next());
					}
				}
			}
			
			System.out.print("#"+tc+" ");
			for(int i=0; i<n; i++) {
				if(!(q1.isEmpty()) && i%2==0) {
					System.out.print(q1.poll()+" ");
				}else if(!(q2.isEmpty()) && i%2!=0){
					System.out.print(q2.poll()+" ");
				}
			}
			System.out.println();
		}
	}

}
