
public class palindrome {

	public static void main(String[] args) {
		String line = "levael";
//		int i = 0;
//		int j = line.length()-1;
		
		boolean isPal= true;
		for(int i=0, j=line.length()-1; i < line.length()/2; i++, j--) {
			if(line.charAt(i) != line.charAt(j)) {
				isPal = false;
				break;
			}
		}
		
		System.out.println(isPal);
		
	}
	
	public static boolean isPal(String line) {
		boolean isPal= true;
		for(int i=0, j=line.length()-1; i < line.length()/2; i++, j--) {
			if(line.charAt(i) != line.charAt(j)) {
				isPal = false;
				break;
			}
		}
		return isPal;
	}
}
