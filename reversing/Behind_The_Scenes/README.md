# invalidInstructionException() > UD2 assembly instruction 

## Challenge Description

After struggling to secure our secret strings for a long time, we finally figured out the solution to our problem: Make decompilation harder. It should now be impossible to figure out how our programs work!

## Writeup 

This was a very easy rated reversing challenge from HackTheBox. I was able to solve by going through the initial steps that I generally do for a reversing challenge.  

## Solution Overview

To solve this challenge, I followed these steps:

1. Ran file on the binary to identify the type of file we are looking at.
2. Next, I ran strings on the binary to print all the associated strings.
3. Lastly, I ran hexdump: ```hexdump -C binary``` which revealed the password/flag in the hex code. 

## Ghidra 
We can also see the results in Ghidra. By follwing the Ivalid Instruction Exception to the UD2 instruction, which reveals the hardcoded password.

<img src= ghidra.PNG> 
