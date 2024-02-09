# HTTP Parameter Pollution

## Website 

<img src= "HTBank_Website.PNG">

## Description

I found this challenge to be pretty fun. I was lucky enough to attempt it after the description for the challenge had been updated. I imagine I would have been scratching my head for a bit otherwise. With that description, we know that in order to get the flag we need to withdraw 1337 HTB credits. We have the ability to create a user using /register and the ability to login using /login. So, I created the user rosepwns and logged in. Looking at my Bursuite proxy traffic, I noticed a GET request to an API, api.etherscan.io. The request checks the balance of a crypto wallet (HTBank) using their API key, and the response shows the balance. I think it would have made more sense for this to be the value we needed to withdraw to get the flag. Anyway, we can input out own accounts address and see the expected result of "0". After looking through the API documentation, I didn't see anything super useful. Moving on, I captured the request for withdrawing credits and sent it to the repeater. We can get three different responses based on our value in "amount". The messages being: only numbers are accepted, we can't supply 0, and we don't have enough credits for anything over zero. After some research about potential vulnerabilities with the information observed so far, I decided to try parameter pollution on the application to overide the value I give with the value we know we want. So, I added another amount parameter to the POST request, set the 1st amount to "0" (we know we shouldn't be able to provide this value, and the second amount to the value we want to retrieve "1337". And boom! 200 response code. 

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

## ChatGPT
Looking for vulnerabilities inside the source code with the help of ChatGPT:
<br>
<img src= "chatgpt_exploitation.PNG">



## Exploit
Exploiting the HPP vulnerability: 
<br>
<img src= "burp_request.PNG">

## More Information
[HTTP Parameter Pollution](https://book.hacktricks.xyz/pentesting-web/parameter-pollution)
<summary> The impact of this vulnerability is that it allows attackers to bypass account restrictions and pull money not from their account, but from the bank directly.</summary>



