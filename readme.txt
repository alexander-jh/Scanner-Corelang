Project:	Project 1
Author:		Alexander Hoke
Date:		01/20/2021

------------------------------------- INCLUDED -----------------------------------------
Makefile				-	Build file for dynamic library.
lib_token.hpp				-	Header file for external lib
lib_token.cpp				-	Source code for external lib
lib_token.so 				-	Dynamicly compiled library
Core.py 				-	Supplied enumeration file
Main.py   				-	Supplied main function body
Scanner.py 				-	Script links external lib and executes
					-	scanner functions

----------------------------------- INSTRUCTIONS ----------------------------------------
The lib_token.so library is pre-compiled in std-linux and is included so unless you're 
running via a different a OS/distro you *shouldn't* have to recompile.  

If you do have to/choose to recompile the dynamic library Makefile is included just run:
```make```
```make clean```

Full compiler options (annotations below):
```g++ -Wall -shared -fPIC -std=c++11 lib_token.cpp lib_token.hpp -o lib_token.so 
		-lboost_regex```
	-Wall		Enables additional compiler flags
	-shared		Directs compiler that object files are shared enabling linking
	-fPIC		Genereates position-independent code which is machine code
			   which can be executed agnostic of memory addressing
	-std=c++11	Specify C++ version, unfortunately the most modern version
			   on std-linux is 11. Advantage of 11 is addition of auto,
			   lambda functions, direct looping over iterators, smart
			   pointers, and variable argument functions yet >=14 is 
			   optimal.
	-lboost_regex	Links the Boost/Regex.hpp library. Boost contains a variety
			   of open source libraries which are portable and not
			   OS dependent. While C++11 does introduce the std::regex 
			   library, it won't compile with GCC version < 4.9. 

To run the base program simply run:
```python3 Main.py <<*file_name*>>```
or
```./tester.sh```
if it fails to execute due to permissions
```chmod +x tester.sh```


----------------------------------- METHODOLOGY ------------------------------------------
For the sake of this project, an external C++11 library implements core functions using 
the standard Python CTypes wrapper. CTypes is capable of wrapping either C or C++ given 
an ```extern "C"``` arguement since all code is treated equally as C from Python.

The wrappers work by passing arguements from Python to C/C++ and vice verse using shared 
memory space. CTypes requires the library be dynamically linked and the function return 
types (or parameters) to be specified. Additionally any non-standard data structures,
ie structs, must be formally defined in Python. Special care must be taken to decode string 
variables prior to and following passing since all C/C++ string/char types are UTF-8 by 
by default while Python is built on byte strings which are inherently different and will 
cause issues if not managed.

The rationale behind using C++ over souly Python for the Scanner is that Python is an 
interpretted language, hence it is further from the kernel and will not execute the 
necessary system calls for I/O as quickly. Additionally libraries are loaded into main
memory, as well as the ability to pre-declare shared memory space. Lastly statically
declared variables are reserved when the library is loaded, so static inline functions
and static objects (like unordered_map used here) will substantially out perform 
Python.

Boost regex library used since std-linux still uses GCC v4.8.5 which is roughly from 
06/23/2015.
