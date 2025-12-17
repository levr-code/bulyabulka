Thebulka – A Whimsical Esoteric Language
Thebulka is an esoteric programming language themed around baking. It uses a central accumulator n, named variables, string and numeric operations, and playful “ingredient”-based syntax.
Overview

Type: Esoteric programming language

Designer: [levr-code]
Release: 2025
Paradigm: Accumulator-based, line-oriented, string & numeric operations
Purpose: Fun, experimentation, exploring unconventional programming models
The main variable n can hold strings, characters, or numbers. Named variables are stored in a dictionary vars.
Core Syntax
Input / Output

<bulk>      # Reads user input
<buluka>    # Substitutes the current value of n
<random>    # Inserts a random float between 0 and 1
bulka       # Prints the current value of n

Accumulator Operations

mya<text>   # Appends text to n (supports <varname>)
+bul / -bul # Increment/decrement ASCII value of n (single-character only)
Arithmetic (stored in vars["math"])
/bulu X Y   # Addition
/blu X Y    # Subtraction
/bul X Y    # Multiplication
/lub X Y    # Division
/lbu X Y    # Modulo
Variables:
mac<varname> <value>   # Assigns <value> to <varname>
<varname>               # Access variables via <varname> syntax
Loops & Conditionals
/bul/ N:               # Repeat block N times (numeric N)
?bul?:<X>:<operator>:<Y>:   # String comparison block
?lub?:<X>:<operator>:<Y>:   # Numeric comparison block
Indentation: 4 spaces per level
Random Numbers
/bulr varname min max  # Assign random integer to varname
Example Programs
1. Hello User
macgreeting <bulk>
myaHello, <greeting>
bulka
Description: Reads user input into greeting, appends "Hello, " + input to n, and prints it.
Input: "Alice" → Output: Hello, Alice
2. Conditional Greeting
macinput <bulk>
?bul?:<input>:==:Hello:
    myaHi there!
bulka
Description: Checks if user input is "Hello"; appends "Hi there!" if true.
4. Loop Example
/bul/ 3:
    myaHello!
bulka
Description: Repeats "Hello!" 3 times and prints accumulated n.
5. Numeric Operations
/bulu 5 10
/blu 20 4
/bul 3 7
/lub 20 4
/lbu 10 3
Description: Adds, subtracts, multiplies, divides, and calculates modulo — results stored in vars["math"].
6. Random Number Assignment
/bulr randomValue 1 100
myaRandom value is <randomValue>
bulka
Description: Assigns a random integer between 1 and 100 to randomValue and prints it.
Philosophy
Thebulka encourages playful syntax and experimentation. Its design revolves around baking metaphors, string/accumulator manipulation, and whimsical programming patterns, making it a fun esoteric language to explore
