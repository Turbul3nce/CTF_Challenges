# WAF Bypass > SQL Injection

## Website 

<img src= "website.png">

## Description



## Set Up

1. Burpsuite proxy and Repeater.
2. Read through the source code to understand how our requests are being handled.
3. Read up on transfer enoding after finding the vulnerability in the code. See more information.

## Burpsuite
Testing chunked transfer encoding using Burpsuite. Looking for an Internal Server Error:
<br>
<img src= "burpsuite_repeater.png">



## Exploit
Automating the SQLi exploitation with SQLMap: 
<br>
<img src= "exploit_withj_sqlmap.png">

## More Information
[Transfer-Encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Transfer-Encoding)
<summary> The impact of this vulnerability is that it allows attackers to bypass implemented WAF and pull down all information from a database.</summary>

