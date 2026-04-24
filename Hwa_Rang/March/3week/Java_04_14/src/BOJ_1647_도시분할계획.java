import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Edge implements Comparable<Edge>{
	int left, right, cost;

	public Edge(int left, int right, int cost) {
		this.left = left;
		this.right = right;
		this.cost = cost;
	}
	
	
	//우선순위 큐를 위한 compareTo
	@Override
	public int compareTo(Edge o) {
		// TODO Auto-generated method stub
		return this.cost - o.cost;
	}
	
}

public class BOJ_1647_도시분할계획 {
	
	static int[] p;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st =  new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		p = new int[n+1];
		for(int i=1; i<=n; i++) {
			p[i] = i;
		}
		
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int left = Integer.parseInt(st.nextToken());
			int right = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());
			
			pq.add(new Edge(left, right, cost));
		}
		
		int sum = 0;
		int max = 0;
		int cnt = 0;
		for(int i=0; i<m; i++) {
			Edge e = pq.poll();
			
			if(findSet(e.left) != findSet(e.right)) {
				union(e.left, e.right);
				sum += e.cost;
				if(max < e.cost) max = e.cost;
				cnt++;
			}
			
			if(cnt == n-1) break;

		}
		
		System.out.println(sum-max);
	}
	
	static void union(int a, int b) {
		p[findSet(b)] = p[findSet(a)];
	}
	
	static int findSet(int n) {
		if(n != p[n]) p[n] = findSet(p[n]);
		
		return p[n];
	}
	
}
