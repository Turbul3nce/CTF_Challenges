# Server-Side Template Injection

## Description

We know the flag can be found at the message/3 endpoint. The vulnerability in this challenge involves the host header, specifically permitting the manipulation of the "X-Forwarded-Host". This manipulated value is reflected in the href tag within the website's response, leading to believe it may be vulnerable to web cache poisoning. Testing with Burpsuite collaborator revealed the interaction of GET requests for files normally loaded by the latters page, such as main.css and viewletter.js. The approach to solving this leverages the vulnerability by setting up a web server using localhost.run, a service that comes with SSH, allowing you to expose a local web server to the internet temporarily. With this, we can host a malicious version of the website's "viewletter.js" file that will get loaded by the letters page. The attack revolves around deceiving the website into loading the manipulated "viewletter.js" file through the poisoned cache, which includes an internal GET request targeting the typically restricted endpoint message/3, and a subsequent POST request to the "/submit" endpoint with the response data from the GET request, revealing the contents of the "hidden" message 3 in our new id.

## Set Up

1. Burpsuite Repeater: GET requests to /letters?id=new & POST request to /submit.
2. Apache2 server hosting main.css & viewletter.js(malicious).
3. Tunnel using `ssh -R 80:localhost:80 localhost.run -i /home/$user/.ssh/id_rsa`.

## Exploit

It sends a crafted GET request to the specified target URL, exploiting a vulnerability in the application's handling of user input within the 'text' parameter. The payload utilizes Python's class and method reflection to execute the command 'cat flag.txt', attempting to read and print the contents of a 'flag.txt' file on the server.

## More Information

[SSTI in Flask(Jinja2)](https://kleiber.me/blog/2021/10/31/python-flask-jinja2-ssti-example/)
