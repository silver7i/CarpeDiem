import java.util.Scanner;

public class SWEA_1231_중위순회 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		for(int t=1; t<=10; t++) {
			int v = Integer.parseInt(sc.nextLine());
			String[] arr = new String[v+1];
			
			for(int i=1; i<v+1; i++) {
				arr[i] = sc.nextLine().split(" ")[1];
			}
			System.out.print("#"+t+" ");
			inOrder(arr, 1, arr.length);
			System.out.println();
		}
	}
	
	public static void inOrder(String[] tree, int v, int N) {
		if(v>=N || tree[v] == null) return;
		//왼자탐색
		inOrder(tree, v*2, N);
		System.out.print(tree[v]);
		//오자탐색
		inOrder(tree, v*2+1, N);
	}

}
