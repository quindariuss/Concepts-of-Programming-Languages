# Question One
Explain why is a context-free grammar important. Provide an example 
Explain the general structure of a grammar. Provide an example 
Context free grammar is important because is the backbone of programming languages without such a grammar communication with machines would be a lot harder. 
To have a computer understand Natural Language on the machine code level would be an insanely hard challenge to deduce with all the rules and regulations of English but context free grammars allow it to simplified greatly. 
# Question Two 
In the given grammar below, indicate the terminals. Explain. 
Explain the differences between developing a scanner and implementing a scanner.

<assign> -> <id> = <expr>

<id> -> A | B | C

<expr> -> <expr> + < term> | <term>

<term> -> <term> * <factor> | <factor>

<factor> -> ( <expr>  ) | <id>

## Answer 
A, B and C are the given terminals because they cannot be derived any further.

Developing a scanner and Implementing a scanner, assuming developing is the work done before implementation. 
In development you have to mark your keywords, comment strings and the general rules of the grammar and compile that its a form for you then to work off of to produce an implementation of the scanner. 
You can't implement a scanner without developing it first. 

# Question Three
How do you include keywords and identifiers in grammar rules? Explain. 
What are the differences between left and right-most derivations? Explain.  What are the advantages and disadvantages of defining the keyword and symbol tables in the scanner or the parser? Explain. 
## Ans
a:
Including keywords and identifiers in grammar rules are done by allowing them to be terminals within the grammar and not allowing any further derivations.
b:
Left-most derivations expand the leftmost non-terminal.
Right most derivations expand the rightmost non-terminal.
c:
Symbol Table

Advantages:
- can create a database of identifiers making the symbol table easier to search 
- check to see if the symbols have been defined
- can store all the symbols in one place 
Disadvantages: 
- tough to implement 


# Question Four
Explain the advantages/disadvantages of a compiler and an interpreter. 
Explain what are the differences in the structure of a compiler and an interpreter. 
## Ans
Briefly explain the runtime efficiency of an object-oriented programming program vs a non object-oriented program.
a: 
Compiler: 
adv: 
executes faster
easier on the machine once compiled 
dis:
harder to write
not flexible

Interpreter
adv: 
easier to understand and write 
very flexible, can have different programming paradigms 

dis: 
slower than compiled languages

b: 
A complier translates an input program into machine code 
An interpreter translates the input program one line at a time and executes it in a sort of a virtual machine implemented in a complied language 
c: 
Non-object oriented programing is said to perform really well at applications with limited scope or more functional oriented but they don't do well with programs where the object is being mutated many times which is where OOP works best.
# Question Five
Briefly explain the differences between syntax trees and derivations. 
Explain how the lexical  rules are used to develop a lexical analyzer.
# Question Six
Explain how lexical analysis helps in developing a scanner.  
What data does the scanner provide to the parser? Explain.
# Question Seven
Given the following grammar, 
Show that the grammar is ambiguous. 
Write a leftmost derivation for the sentence bbaaba. 
Construct a parse tree for the sentence bbaaba.
S -> Sa | SSb | b | ε
# Question Eight
Explain a simple technique or approach to add simple semantics to syntax rules. 
What language features can be specified with this technique?
# Question Nine
Briefly explain the concept of dynamic memory allocation and de-allocation. Provide a simple example in Java. 
Explain how some simple semantic specification is included in the overall syntax rules. 
Include  examples.
