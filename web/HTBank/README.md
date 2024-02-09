# HTTP Parameter Pollution

## Website 

<img src= "HTBank_Website.PNG">

## Description



## Set Up

1. Burpsuite Repeater.
2. Read through the source code (unnecessary now that value needed is in the description).
3. Read through the etherscan API documentation (unnecessary). 
4. POST to /api/withdraw before being exploiting:
  ```html
-----------------------------55942694529039672783834867755

Content-Disposition: form-data; name="account"
value

-----------------------------55942694529039672783834867755

Content-Disposition: form-data; name="amount"
value
-----------------------------55942694529039672783834867755--
```

## ChatGPT
Looking for vulnerabilities inside the source code with the help of ChatGPT:
<br>
<img src= "chatgpt_exploitation.PNG">



## Exploit
Exploiting the HPP vulnerability: 
<br>
<img src= "burp_request.PNG">

## More Information
[HPP](https://book.hacktricks.xyz/pentesting-web/parameter-pollution)
<summary> The impact of this vulnerability is that it allows attackers to bypass account restrictions and pull money not from their account, but from the bank directly.</summary>



