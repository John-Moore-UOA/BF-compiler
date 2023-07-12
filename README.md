# BF-compiler
BF coding langauge compiler written in python

BF is a simple language of { + - > < . [ ] } along a tape of some length

\+ : increment current cell value

\- : decrement current cell value

\. : output value at current cell

\> : Shift pointer to tape +1

\< : Shift pointer to tape -1

\[ : Loop bracket open

\] : Loop bracket close



74
\>++++++[>++++++++++++<-]>++.   => J

79
\>++++++[>+++++++++++++<-]>+.   => O

72
\>++++++[>++++++++++++<-]>.     => H

78
\>++++++[>+++++++++++++<-]>.    => N


Example: 
\>++++++[>++++++++++++<-]>++.  
Pseudo-Code:
+ Shift to pointer to cell 2
+ increment cell 2 to value of 6 (this cell will be used as an incrementor for the loop)
+ Loop
+ Move back to cell 1
+ Increment to value of +10
+ move foward to cell 2 and decrement
+ Repeat until cell 2 value is 0
+ Shift to cell 2 increment +2
+ print ASCII value of cell 2



