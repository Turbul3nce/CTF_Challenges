Title: Vulnerable Host Header => Web Cache Poisoning

Description: 
The vulnerability in this challenge involved the host header, specifically permitting the manipulation of the "X-Forwarded-Host". 
This manipulated value found its reflection in the href tag within the website's response, ultimately leading to an attack vector known as web cache poisoning.
Testing with Burpsuite collaborator showed the interaction of the GET requests for files noramlly loaded locally, such as main.css and viewletter.js.
My approach hinged on leveraging this vulnerability by setting up a web server hosting a malicious version of the website's "viewletter.js" file.
I achieved this by using localhost.run which comes as a service with ssh, it allows you to expose a local web server, typically running on your machine, to the internet temporarily.
The crux of the attack revolved around deceiving the website into serving the manipulated "viewletter.js" file through the poisoned cache. 
Embedded within this JavaScript file was an internal GET request targeted at a the typically restricted endpoint message/3, and then a POST request to the "/submit" endpoint with the data from the message/3. 
So, to poison the cache, we can make GET request with our malcious headers to a non-exsistent id, sucessfully poisoning the cache with our attacker url. Then we make a POST request to /submit.
The submit endpoint will make a request automatically to the new poisoned id. We can navigate to the new id to find the contents of the "hidden" message 3.  
