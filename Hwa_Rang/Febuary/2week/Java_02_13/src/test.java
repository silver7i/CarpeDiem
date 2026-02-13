public class test {
	public static final double TABLE_WIDTH = 254L;
	public static final double TABLE_HEIGHT = 127L;
	public static final double BALL_RADIUS = 5.73 / 2;
	
	
	public static void main(String[] args) {
		
		double[] ball_0 = {64.0, 64.0};
		double[] ball_1 = {250.0, 122.0};
		
		//theta구하기
		
		double width = ball_1[0] - ball_0[0];
		double height = ball_1[1] - ball_0[1];
		
		double rad = Math.atan2(width, height);
		double angle = Math.toDegrees(rad);
		
		System.out.println(angle);
	}
}
