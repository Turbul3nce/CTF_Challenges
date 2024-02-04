# Server-Side Template Injection

## Description

The website takes user input and spits it out in several different formats. The vulnerability arises in the user input within the 'text' parameter which isn't sanitized by the web application, allowing us to inject Python code into server-side templates. Exploiting this vulnerability enables the execution of arbitrary commands.

## Framework 

- Flask
  
## Exploit

It sends a crafted GET request to the specified target URL, exploiting a vulnerability in the application's handling of user input within the 'text' parameter. The payload utilizes Python's class and method reflection to execute the command 'cat flag.txt', attempting to read and print the contents of a 'flag.txt' file on the server.

## More Information

[SSTI in Flask(Jinja2)](https://kleiber.me/blog/2021/10/31/python-flask-jinja2-ssti-example/)
