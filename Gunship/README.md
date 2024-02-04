# Vulnerable Host Header => Web Cache Poisoning

## Framework

- Node

## Description

We know the flag can be found at the message/3 endpoint. The vulnerability in this challenge involves the host header, specifically permitting the manipulation of the "X-Forwarded-Host". This manipulated value is reflected in the href tag within the website's response, leading to believe it may be vulnerable to web cache poisoning. Testing with Burpsuite collaborator revealed the interaction of GET requests for files normally loaded by the latters page, such as main.css and viewletter.js. The approach to solving this leverages the vulnerability by setting up a web server using localhost.run, a service that comes with SSH, allowing you to expose a local web server to the internet temporarily. With this, we can host a malicious version of the website's "viewletter.js" file that will get loaded by the letters page. The attack revolves around deceiving the website into loading the manipulated "viewletter.js" file through the poisoned cache, which includes an internal GET request targeting the typically restricted endpoint message/3, and a subsequent POST request to the "/submit" endpoint with the response data from the GET request, revealing the contents of the "hidden" message 3 in our new id.

## Exploit

The script takes advantage of a prototype pollution vulnerability in a web application. It sends a POST request to the '/api/submit' endpoint, injecting a payload that pollutes the 'proto' property with a 'block' object containing a command for child process execution (id > static/images/win.txt). Subsequently, it triggers this payload with a GET request to '/static/images/win.txt', attempting to execute the command and retrieve the output, showcasing the impact of the prototype pollution vulnerability.

## More Information

[Host Header Attacks](https://portswigger.net/web-security/host-header)

