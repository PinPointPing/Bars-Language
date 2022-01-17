# Bars-Reader
This python code will generate and read the language "Bars"; a language I came up with based off of how computers store data.

This works by having a combination of 0's and 1's. 0 meaning OFF and 1 meaning ON.

We have a sequence of 0's and 1's turning ON and OFF a sequence of 16, 8, 4, 2, 1. All multiples of 2.


Let's write the letter A:

We get the number in the alphabet that "A" occupies which is 1. So we turn 1 ON.

16, 8, 4, 2 OFF, 1 ON. So we get:

00001 = A


To make the letter B:

We get the number in the alphabet that "B" occupies which is 2. So we turn 2 ON.

16, 8, 4 OFF, 2 ON, 1 OFF.

00010 = B


Now it get's tricky. What about letters which aren't multiples of 2, for example C?

We get the number in the alphabet that "C" occupies which is 3. So we turn 1 ON AND 2 ON because 1 + 2 = 3.

16, 8, 4 OFF 2, 1 ON

00011 = C


To generate sticks we create a short line for a 0, and a tall line for a 1, and to separate letters we just split the sequence every 5 numbers.
0100001001 = HI
