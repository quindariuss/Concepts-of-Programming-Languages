#include <stdio.h>

main()
{
	printf("---Trapezoid Area Computer---\n");
	int top_base, bottom_base, height; 
	printf("Enter the top base of Trapezoid: ");
	scanf("%d", &top_base);
	printf("Enter the bottom base of Trapezoid: ");
	scanf("%d", &bottom_base);
	printf("Enter the height of Trapezoid: ");
	scanf("%d", &height);
	double area = ((top_base + bottom_base)/2)*height;
	printf("The area of the Trapexoid is: %f", area);
	return 0;
}
