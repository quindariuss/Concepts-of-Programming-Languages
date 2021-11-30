#include <stdio.h>
#include <string.h>
int main ()
{
	int index;
	int word_count = 12;
	char words[word_count][45];

	for (index = 0; index < word_count; index++)
	{
		scanf("%s", words[index]);
	}

	for (index = 0; index < word_count; index++)
	{
		printf("%s \t\t|--> index: %i", words[index], index);

		if(!strcmp("LET",words[index]))
		{
		printf("\t\t\tEXPRESSION: LET");
		}
		else if(!strcmp("IF",words[index]))
		{
		printf("\t\t\tEXPRESSION: IF");
		}
		else if(!strcmp("+",words[index])||!strcmp("*",words[index])||!strcmp("/",words[index])||!strcmp("-",words[index])||!strcmp("=",words[index]))
		{
		printf("\t\t\tEXPRESSION: OPERATOR");
		}
		else
		{
		printf("\t\t\tIDENTIFIER");
		}

		printf("\n");
	}
}

