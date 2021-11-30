#include <stdio.h>
#include <ctype.h>
#include <string.h>
// A structure to hold the values of a symbol.
struct symbol 			
{
	char word[45];
	char type[30];
	char type_details[30];
	int index;
};
/*Probably wont even use this*/
struct let
{
	/*
	   0 is false 
	   1 is true
	 */
	int isword;
	char value[100];
	int numvalue;
};

int main(void)
{
	int index;
	int subindex;
	int global_index;
	int word_count = 68;
	char words[word_count][45];

	/*Array of Structures*/
	struct symbol symbols[12];

	for (index = 0; index < 68; index++)
	{	
		scanf("%s",words[index]);
	}

	global_index = 0;
	for (index = 0; index < 12; index++)
	{
	for (subindex = 0; subindex < 5; subindex++)
	{	
		global_index++;
		printf("%s\n",words[index]);
		if (!strcmp("0",words[index]) ||!strcmp("1",words[index]) ||!strcmp("2",words[index]) ||!strcmp("3",words[index]) ||!strcmp("4",words[index]) ||!strcmp("5",words[index]) ||!strcmp("6",words[index]) ||!strcmp("7",words[index]) ||!strcmp("8",words[index]) ||!strcmp("9",words[index]) ||!strcmp("10",words[index]) ||!strcmp("11",words[index]) ||!strcmp("12",words[index]) ||!strcmp("13",words[index]) ||!strcmp("14",words[index]) ||!strcmp("15",words[index]) ||!strcmp("16",words[index]) ||!strcmp("17",words[index]) ||!strcmp("18",words[index]) ||!strcmp("19",words[index]) ||!strcmp("20",words[index]) ||!strcmp("21",words[index]) ||!strcmp("22",words[index]) ||!strcmp("23",words[index]) ||!strcmp("24",words[index]) ||!strcmp("25",words[index]) ||!strcmp("26",words[index]) ||!strcmp("27",words[index]) ||!strcmp("28",words[index]) ||!strcmp("29",words[index]) ||!strcmp("30",words[index]) ||!strcmp("31",words[index]) ||!strcmp("32",words[index]) ||!strcmp("33",words[index]) ||!strcmp("34",words[index]) ||!strcmp("35",words[index]) )
		{
			printf("Number?\n");
		}
		else if (!strcmp("LET",words[global_index]))
		{
			printf("We gotta let\n");
		}
		else if (!strcmp("OPERATOR",words[global_index]))
		{
			printf("We gotta op\n");
		}
		else if (!strcmp("EXPRESSION",words[global_index]))
		{
			printf("We gotta expression\n");
		}
		else if (!strcmp("IDENTIFIER",words[global_index]))
		{
			printf("We gotta expression\n");
			break;
		}
	}
}
printf("GLOBAL INDEX:%i",global_index);
}

