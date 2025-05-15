#so here is what i started with -
#first are basic dataTypes and Syntax...

'''
* so it started with this
variables don't need to be explicitly be declared, we just name a variable and go with the value it stores, Python just knows what dataType it has so its easy... damnnn

* Python has DataTypes - Int, String, Bool, Float... 
well thats easy to say, but when i found what type of dataTypes are there... Damnnn...
1. There are Basic DataTypes (mentioned above),
2. Text type such as String,
3. Sequence Types include (list, tuple, range), 
4. set Type (set, frozenset), mapping Type (dict), 
5. Binary Types (bytes, bytearray, memoryview), 
6. noneType (NoneType)
         
         ~_~ Such wide range of Implementation... for now, lets just start with baisc ones
'''


X = 23
name = "DeluluKid"
BoolVar = True
floatingNum = 2.34443212

# I was trying to concatinate this variables and realised the string and numbers can't be concatinated. so i found the approach of f"{}" f-string, used for better concatination of string and numbers - a much much better apporach i guess...
print(f"This are just Exmaples: {X}, {name}, {BoolVar},  {floatingNum}")


"""
next i learned about, TypeConversion and TypeCasting
2 types in this - one is Implicit and Other is Explicit ---
    implicit automatically converts one dataType to another, while Explicit is manual.

here is the example for you to understand - a + b are int and Float, and when we check what the result variable Type is. it will say FLOAT. as it was implicitly converted by python...

but when i do bool() it explicitly changes the dataType of res. and the output we get is True, since in python any non-zero number is true by default...
"""

a = 0     # int
b = 0    # float

result = a + b  # a is automatically converted to float
print(result)
print(type(result))

res = bool(result)
print(res)
print(type(res))


"""

I also went ahead and learn many more things like INPUT and OUTPUT,  for output its Print(), but for input() we use a variable and input() to get input from user...  
    eg: name = input("Enter your Name")


also i know about operators and Controls due to my little Knowledge of javaScript
Operators
Arithmetic operators (+, -, *, /, //, %, **)
Assignment operators (=, +=, etc.)
Comparison operators (==, !=, >, <, etc.)
Logical operators (and, or, not)

    but the extra ones are 
    1. Bitwise Operators (I never Understand these... not that i can't understand them, because i never tried to understand them anyway... i never saw their usage in detail, just know they can perform binary operations...)

    2. Identity Operator (is and isNot) - checking if the 2 varaible refer to as same object like x is y... the answer would be in Bool... same for isNOT just opposite to ask...

    3. Membership Operators(in or notIN) - similar to identity in usage, just used to check if the varaiable or whatever we are checking is in a sequence or not... Sequence are list, tuple, string... 
    list and tuple are like arrays, just list is changeable, but Tuple is UnChangeAble (Stubborn 😾)

Then Comes Operator Precedence - order in which the operators perform operation... like BODMAS... but due to having too many operator, this is a bit tricky to remember. so instead - while implementing just refer to doc, here is a copy of it
   
    1. () — Parentheses
    2. ** — Exponentiation
    3. +x, -x, ~x — Unary plus, minus, bitwise NOT
    4. *, /, //, %
    5. +, -
    6. <<, >>
    7. &
    8. ^
    9. |
    10. ==, !=, >, <, >=, <=, is, in, not in
    11. not
    12. and
    13. or
    14. =, +=, -=, etc.

    

THEN IS CONTROL statements - IF, ELSE, and IF-ELSE LADDER... no need to tell similar to other languages...


"""

# then are LOOPS - 
#     2 main loops -  for and while

###    forLOOP -  
#         for _ITEM_ in Sequence: ## sequence is a list of items... like fruits = ['apple', 'orange'.] -> here is the example
    
fruits = ["apple", "orange"]
for fruit in fruits:
            #do Something - maybe like print them...
            print(fruit)  #Result would be  apple  orange

### whileLOOP
#       while is simple..  just define WHILE (Condition):
#  here is the example
count = 0
while count < 5:
    print(count)
    count += 1


"""

THEN COMES BREAK, CONTINUE, PASS keywords just like other languages, used to operate in loops... 
break - breaks the loop, Continue - Skips that part, and pass just pass (literally does nothing...  just a placeholder, maybe to write code later on...)

there are much more too learn, but I HAD IT ENOUGH>>>

### WELL ITS HARD TO LEARN AND WRITE THINGS HERE AT THE SAME TIME... I THOUGHT I WOULD BE A GOOD IDEA TO KNOW WHAT I AM DOING, SINCE THERE ARE TIMES WHEN BEFORE IMPLEMENTING THINGS, ATLEAST SOME KNOWLEDGE IS NEEDED... SO I THOUGH OF DOING THIS...
BUT THIS TAKES TOO MUCH TIME... LIKE ITS BEEN 2 HOURS, GOING BACK AND FORTH - ITS TAKING TOO MUCH TIME... SO MAYBE I WON'T DO THIS...

I AM ACTUALLY HAVING FUN DOCUMENTING ON THE GO, BUT TOO MUCH TIME CONSUMING AND MAYBE ITS GOOD FOR EARLY DAYS, BUT IT WILL BE HARD LATER ON... LIKE JUST LOOK AT THE NOTES... DAMN, NOT GOOD ENOUGH... SO MANY COMMENTS AND JUST ABRUPT CODE EXAMPLES... 
"""