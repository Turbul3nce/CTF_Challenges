# WAF Bypass > SQL Injection

## Website 

<img src= "website.png">

## Description

. 

## Set Up

1. Burpsuite proxy and Repeater.
2. Read through the source code (unnecessary now that value needed is in the description).
3. Read through the etherscan API documentation (unnecessary). 
4. POST to /api/withdraw before being exploited:
  ```html
-----------------------------55942694529039672783834867755

Content-Disposition: form-data; name="account"
value

-----------------------------55942694529039672783834867755

Content-Disposition: form-data; name="amount"
value
-----------------------------55942694529039672783834867755--
```

## Burpsuite
Looking for vulnerabilities inside the source code with the help of ChatGPT:
<br>
<img src= "chatgpt_exploitation.png">



## Exploit
Automating exploitation with SQLMap: 
<br>
<img src= "exploiting_with_sqlmap.png">

## More Information
[HTTP Parameter Pollution](https://book.hacktricks.xyz/pentesting-web/parameter-pollution)
<summary> The impact of this vulnerability is that it allows attackers to bypass account restrictions and pull money not from their account, but from the bank directly.</summary>

