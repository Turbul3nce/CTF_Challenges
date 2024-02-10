# WAF Bypass > SQL Injection

## Website 

<img src= "website.png">

## Description

This was a fun web challenge. I'll keep it short. The website takes user input in the search parameter. This input is passed to one of two functions depeneding on the Transfer-Encoding. It goes to safe_query if we aren't using chunked transfer-encoding. Safe_query uses a parameterized statement and implements a WAF that filters based on SQL query strings, essentially blocking any SQL injection attempts. But, if we have "Transfer-Encoding: chunked" set, our input is passed

## Set Up

1. Burpsuite proxy and Repeater.
2. Read through the source code to understand how our requests are being handled.
3. Read up on transfer enoding after finding the vulnerability in the code. See more information.

## Burpsuite
Testing chunked transfer encoding using Burpsuite. Looking for an Internal Server Error:
<br>
<img src= "burpsuite_repeater.png">



## Exploit
Saved Burpsuite request to a file. Automated the SQLi exploitation using SQLMap: 
<br>
<img src= "exploit_withj_sqlmap.png">

## More Information
[Transfer-Encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Transfer-Encoding)
<summary> The impact of this vulnerability is that it allows attackers to bypass implemented WAF and pull down all information from a database.</summary>

