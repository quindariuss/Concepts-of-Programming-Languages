import java.util.Scanner;

class trapezoid_area {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("---Trapezoid Area Computer---");
		System.out.print("Enter the top base of Trapezoid: ");
		int top_base = input.nextInt();
		System.out.print("Enter the bottom base of Trapezoid: ");
		int bottom_base = input.nextInt();
		System.out.print("Enter the height of Trapezoid: ");
		int height= input.nextInt();
		double area = ((top_base + bottom_base)/2) * height;
		System.out.println("The area of the Trapezoid is: " + area );
	}
}
