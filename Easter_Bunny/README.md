# Vulnerable Host Header => Web Cache Poisoning

## Description

We know the flag can be found at the message/3 endpoint. The vulnerability in this challenge involves the host header, specifically permitting the manipulation of the "X-Forwarded-Host". This manipulated value is reflected in the href tag within the website's response, leading to believe it may be vulnerable to web cache poisoning. Testing with Burpsuite collaborator revealed the interaction of GET requests for files normally loaded locally, such as main.css and viewletter.js. The approach to solving this leverages the vulnerability by setting up a web server using localhost.run, a service with SSH that allows exposing a local web server to the internet temporarily, and hosting a malicious version of the website's "viewletter.js" file that gets loaded with the letters page. The attack revolves around deceiving the website into loading the manipulated "viewletter.js" file through the poisoned cache, which includes an internal GET request targeting the typically restricted endpoint message/3, and a subsequent POST request to the "/submit" endpoint with the response data from the GET request completes the exploitation, revealing the contents of the "hidden" message 3.

## Set Up

1. Burpsuite Repeater: GET requests to /letters?id=new & POST request to /submit.
2. Apache2 server hosting main.css & viewletter.js(malicious).
3. Tunnel using `ssh -R 80:localhost:80 localhost.run -i /home/$user/.ssh/id_rsa`.

## Exploit

It generates a random ID and sends a GET request to `http://{base_url}/message/{random_id}`, extracting the "count" field from the JSON response. The script then constructs a URL for `http://{base_url}/letters?id={id_}` and sends a GET request with our headers, attempting to manipulate the cache. Debugging information is printed, and success or failure is determined by whether the response text contains the specified value in the "X-Forwarded-Host" header. The `hack()` function orchestrates this process, incrementing IDs, making cache requests, and ultimately sending a POST request to `http://{base_url}/submit` with a predefined message. Debugging details for the submit request are printed.
