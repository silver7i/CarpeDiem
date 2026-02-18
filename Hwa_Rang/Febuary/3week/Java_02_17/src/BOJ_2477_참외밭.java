import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BOJ_2477_참외밭 {
	static int a_h, a_w, b_h, b_w;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] d = new int[6];
		int[] m = new int[6];
		int[] count = new int[5];
		List<Integer> b_h_w = new ArrayList<>();
		List<Integer> a_h_w = new ArrayList<>();
		
		int n = sc.nextInt();
		
		for(int i=0; i<6; i++) {
			d[i] = sc.nextInt();
			count[d[i]]++;
			m[i] = sc.nextInt();
		}
		
		for(int i=0; i<5; i++) {
			if(count[i] == 1) a_h_w.add(i);
			if(count[i] == 2) b_h_w.add(i);
		}	
		
		for(int i=0; i<6; i++) {
			if(d[i] == a_h_w.get(0)) a_h = m[i];
			if(d[i] == a_h_w.get(1)) a_w = m[i];
			if(d[i] == b_h_w.get(0)) {
				if(i == 0 && d[1] == b_h_w.get(1) && d[5] == b_h_w.get(1)) {
					b_w = m[0];
				}
				
				else if(i == 5 && d[4] == b_h_w.get(1) && d[0] == b_h_w.get(1)) {
					b_w = m[5];
				}
				
				else if(i>0 && i<5 && d[i-1] == b_h_w.get(1) && d[i+1] == b_h_w.get(1)) {
					b_w = m[i];
				}
			}
			
			if(d[i] == b_h_w.get(1)) {
				if(i == 0 && d[1] == b_h_w.get(0) && d[5] == b_h_w.get(0)) {
					b_h = m[0];
				}
				
				else if(i == 5 && d[4] == b_h_w.get(0) && d[0] == b_h_w.get(0)) {
					b_h = m[5];
				}
				
				else if(i>0 && i<5 && d[i-1] == b_h_w.get(0) && d[i+1] == b_h_w.get(0)) {
					b_h = m[i];
				}
			}			
			
		}
		
		System.out.println((a_h * a_w - b_h * b_w) * n);
		
	}
	
}
