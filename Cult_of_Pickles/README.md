# Pickle Deserialization => SQL Injection

## Description

The application presents vulnerabilities in both SQL injection and insecure deserialization, specifically with Python's Pickle module. To exploit these weaknesses and achieve remote code execution on the application server, we construct a script. This script serializes our payload using the Pickle module and then embeds it within our SQL injection payload. Upon deserialization on the server side, our payload is executed, effectively chaining these vulnerabilities and granting us remote code execution capabilities. 

## Exploit

This exploit script abuses two vulnerabilities, SQL injection and insecure deserialization in the web application. It creates a specially crafted payload using Python's pickle module, which is then serialized, base64 encoded, and appended to a URL parameter during a GET request. The payload, when deserialized on the server side, invokes the os.system method with a command (cat flag.txt > application/static/flag.txt), allowing us to read the contents of the 'flag.txt' file on the server. The script demonstrates exploitation by chaining together two vulnerabilities and retrieving the contents of the exploited file from the target URL.

## More Information

[Pickle - Insecure Deserialization](https://blog.securelayer7.net/insecure-deserialization-attack-in-python-application/)
