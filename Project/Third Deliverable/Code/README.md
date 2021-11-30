# Building 
```
cc lexer.c -o lexer
cc parser.c -o parser
```

# Running 
```
./lexer <ANY BASIC FILE> | ./parser
```

## Notes 
- Accepts input files of any format 
- Will give a line by line showing  of all tokens
- Will return count of tokens 
> Parser Updates
- Will give you a symbol table for the given file.
