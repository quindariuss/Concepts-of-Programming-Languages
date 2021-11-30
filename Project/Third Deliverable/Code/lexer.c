	int character, 				// Gets individual character input
	    tokens, 				// Count of tokens
	    state;				// Determines if we are inside or outside a word
	state = OUT;
	tokens = 0;
	while ((character = fgetc(fp)) != EOF)	//Loops through the input
	{
		printf("%c",character);
		// If statement to check if we are in a word
		if(character == ' ' || character == '\n' || character == '\t')
		{
			printf("\n");
			state = OUT;
		}
		// If statement to tell if we are starting or finishing a word
		else if(state == OUT)
		{
			state = IN;
			tokens++;
		}
	}
	printf("\nTokens : %d\n",tokens);
	fclose(fp);
	}}

