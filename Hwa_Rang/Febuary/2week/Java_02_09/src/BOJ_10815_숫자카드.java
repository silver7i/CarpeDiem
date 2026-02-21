import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_10815_숫자카드 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader( new InputStreamReader(System.in) );
		
		int n = Integer.parseInt(br.readLine());
		
		int[] cardList = new int[n];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0; i<n; i++) {
			cardList[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(cardList);
		
		int m = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		
		for(int i=0; i<m; i++) {
			int s = Integer.parseInt(st.nextToken());
			System.out.print(binarySearch(cardList, s)+" ");
		}
		
		
	}
	static int binarySearch(int[] arr, int n) {
		int left=0;
		int right = arr.length-1;
		while(left<=right) {
			int mid = (left+right)/2;
			
			if(arr[mid] == n) {
				return 1;
			}
			else if(arr[mid] > n) {
				right = mid-1;
			}
			else {
				left = mid+1;
			}
		}
		
		return 0;
	}
}
