# Command Injection w/ Filter Bypass  

## Description

The challenge is layed out in simple terms and seems pretty starightforward. We can execute commands on the server through a POST request to the run_command endpoint. The problem is that we can only execute commands in the /exectuables directory which is where we are, but there is nothing in this directory. We also cannot traverse the file system because there is a filter blocking the use of .. and /. So We needed to find a way to bypass this filter and execute a command or read the flag somehow. The idea is that we are going to intentioally cause an error by tring to execute the flag.txt as a command and display the output of thsi error in a response, revealing the flag. 

## Set Up
1. Looking at the source code we see that our command gets passed to os.access
<img src= image.PNG> 

## Exploit

. is the only command authorized, as it is internal to bash. you cas see it by writting a single . in the shell :
Image
Almandin — 02/24/2024 1:54 PM
It execute the content of the specified file.
Next,  the :
.''.${HOME:0:1}
 is used instead of :
../
 to bypass the restriction, as the '' are ignored, and the ${HOME:0:1} create a character / because it is the first of the variable HOME.
Then, we try executing the content of flag.txt, generating a mistake : 
Image
Finally, to make the mistake be considered as an output, we must add :
2>&1
## More Information

[SSTI in GO](https://github.com/carlospolop/hacktricks/blob/master/pentesting-web/ssti-server-side-template-injection/README.md)
