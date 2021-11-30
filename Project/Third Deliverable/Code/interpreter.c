#include <stdio.h>
#include <string.h>
// A structure to hold the values of a symbol.
struct symbol 			
{
	char word[45];
	char type[30];
	char type_details[30];
	int index;
};

int main(void)
{
	/*Testing Symbol Structure*/
	struct symbol symbol1;
	strcpy(symbol1.word, "A word goes here");
	strcpy(symbol1.type, "A type goes here");
	strcpy(symbol1.type_details, "A type def goes here");
	symbol1.index = 0;
	
	printf("symbol 1 information: %s", symbol1.word);

	/*Test Array of Structures*/
	struct symbol symbols[10];
	strcpy(symbols[0].word, "A word goes here from an array");
	strcpy(symbols[0].type, "A type goes here");
	strcpy(symbols[0].type_details, "A type def goes here");
	symbol1.index = 0;

	printf("symbol 0 Array Information: %s", symbols[0].word);
}

