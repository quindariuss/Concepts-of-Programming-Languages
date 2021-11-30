#include <stdio.h>
#include <string.h>

int main(void)
{
	int index;
	int symbol-count = 12;
	struct symbol 			// A struct to hold the valeus of a symbol
	{
		char word[45];
		int index;
		char type[30];
		char type_details[30];
	}

struct symbols symbol[symbol-count];
for (index = 0; index < symbol-count; index++)
{
	symbols[index].word = "hello world";
}
}

