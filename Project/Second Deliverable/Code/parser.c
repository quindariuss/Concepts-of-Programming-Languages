#include <stdio.h> 

int main ()
{
	printf("I am the parser");
	char ch; 
	while((ch = getchar() ) != EOF)
	{
		putchar(ch);
	}
}
