# Thebulka

**Thebulka** is an esoteric programming language themed around **baking**. It uses a central accumulator `n`, named variables, string and numeric operations, and playful “ingredient”-based syntax.

---

## Overview

- **Type:** Esoteric programming language  
- **Designer:** [levr-code]  
- **Initial Release:** 2025  
- **Paradigm:** Accumulator-based, line-oriented, string & numeric operations  
- **Purpose:** Fun, experimentation, exploring unconventional programming models  

The main variable `n` can hold strings, characters, or numbers. Named variables are stored in a dictionary `vars`.

---

## Syntax & Semantics
### Comments
- `#this is a comment`
- `#*this is a`
- `multiline comment*#`
### Input / Output
- `<bulk>`  Reads input from the user
- `<buluka>`  Substitutes the current value of `n`
- `bulka`  Prints the current value of `n`
- `bulya`  Clears `n`
### Random Numbers
- `<random>`  Inserts a random float between 0 and 1
- `/bulr NAME MIN MAX` sets variable `NAME` to a random integer betwen `MIN` and `MAX`
### Math
- `/bulu X Y` saves `X`+`Y` to `math` variable
- `/blu X Y` saves `X`-`Y` to `math` variable
- `/bul X Y` saves `X`*`Y` to `math` variable
- `/lbu X Y` saves `X`-`Y` to `math` variable
### Cycles and conditions
- `/bul/ X:` for cycle with X iterations
- `?blu? X:OPERATION:Y:` if X OPERATION Y when
- `?bul? X:OPERATION:Y:` while X OPERATION Y when
### Variables
- `macNAME VALUE` initialises and sets variable `NAME` to `VALUE`
- `<NAME>` finds variable `NAME` and replaces this with its value
### Examples
- #### factorial
```text
maccat <bulk>
macn 1
maci 1
/bul/ <cat>:
    /bul <n> <i>
    macn <math>
    /bulu <i> 1
    maci <math>
    #this is a comment
mya<n>
#*
this is a
multyline
comment
*#
bul#*you can even do this and it will work*#ka
bulya
bulka
```
- #### conditional Hello
```text
mac1nput <bulk>
?bul? 1nput:=:Hi:
    myaHello
bulka
bulya
bulka
```
