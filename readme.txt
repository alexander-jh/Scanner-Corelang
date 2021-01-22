Project:	Project 1
Author:		Alexander Hoke
Date:		01/20/2021

------------------------------ INCLUDED ------------------------------
Makefile				-	Build file for dynamic library.
lib_token.hpp				-	Header file for external lib
lib_token.cpp				-	Source code for external lib
lib_token.so 				-	Dynamicly compiled library
Core.py 				-	Supplied enumeration file
Main.py   				-	Supplied main function body
Scanner.py 				-	Script links external lib and executes
					-	scanner functions

---------------------------- INSTRUCTIONS ----------------------------
The lib_token.so library is pre-compiled and attached for simple link-
ing, but for the sake of completion the C++ source files are included. 

To compile the dynamic library a Makefile is included (but it is not
necessary to run):
```make```
```make clean```

Full compiler options:
```g++ -Wall -shared -fPIC -std=c++11 lib_token.cpp lib_token.hpp -o lib_token.so
	-lboost_regex```

To run the base program simply run:
```python3 Main.py <<*file_name*>>```


---------------------------- METHODOLOGY ------------------------------
For the sake of this project, an external C++11 library implements the
major functions using the standard Python CTypes wrapper. CTypes is
capable of wrapping either C or C++ given an ```extern "C"``` arguement.

The wrappers work by passing arguements from Python to C++ and vice
verse using shared memory space. CTypes requires the library be linked
and the function return types be specified. Special care must be taken
to decode the string variables prior to passing between programs.

The rationale behind using C++ over souly Python for the Scanner is 
that Python is an interpretted language, hence it is further from the
kernel and will not execute the necessary system I/O calls as
efficiently. 

Boost regex library used since std-linux still uses GCC v4.8.5 which
lack support for much C++11 and later functionality.