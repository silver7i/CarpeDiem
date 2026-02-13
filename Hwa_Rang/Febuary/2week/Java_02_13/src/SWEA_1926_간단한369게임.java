import java.util.Scanner;

public class SWEA_1926_간단한369게임 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		
		int n = sc.nextInt();
		
		String[] arr = new String[n]; 
				
		for(int i=0; i<n; i++) {
			arr[i] = ""+(i+1); 
		}
		
		for(String s : arr) {
			if(s.length() == 3) {
				if(s.charAt(0) == '3' || s.charAt(0) == '6' || s.charAt(0) == '9') {
					System.out.print('-');
					if(s.charAt(1) == '3' || s.charAt(1) == '6' || s.charAt(1) == '9') {
						System.out.print('-');
						if(s.charAt(2) == '3' || s.charAt(2) == '6' || s.charAt(2) == '9') {
							System.out.print("-");
						}
					}
				}
				
				else if(s.charAt(1) == '3' || s.charAt(1) == '6' || s.charAt(1) == '9') {
					System.out.print('-');
					if(s.charAt(2) == '3' || s.charAt(2) == '6' || s.charAt(2) == '9') {
						System.out.print('-');
					}
				}
				
				else if(s.charAt(2) == '3' || s.charAt(2) == '6' || s.charAt(2) == '9') {
					System.out.print('-');
				}
				
				
				else System.out.print(s);
				
			}
			
			else if(s.length() == 2) {
				if(s.charAt(0) == '3' || s.charAt(0) == '6' || s.charAt(0) == '9') {
					System.out.print('-');
					if(s.charAt(1) == '3' || s.charAt(1) == '6' || s.charAt(1) == '9') {
						System.out.print('-');
					}
				}
				else if(s.charAt(1) == '3' || s.charAt(1) == '6' || s.charAt(1) == '9') {
					System.out.print('-');
				}
				
				else System.out.print(s);
				
			}
			
			else {
				if(s.equals("3") || s.equals("6") || s.equals("9")) {
					System.out.print("-");					
				}
				else System.out.print(s);
			}
			
			System.out.print(" ");
			
			
		}
	}

}
