# Pickle Deserialization => SQL Injection

## Description

After checking out the website, I notice there is a number that gets randomly generated everytime the page is refreshed. After checking the source code I see a reference to a /debug page. Going here exposed the vulnerable code. 
###
###### `if request.method == 'POST':`
######        `ingredient = request.form.get('ingredient', '')`
######        `recipe = '%s = %s' % (ingredient, request.form.get('measurements', ''))`
###
This part of the source code tells me the measurements in the GET request are stored in recipe, which is later used as a parameter in calc(recipe).  
`def calc(recipe):`
        `global garage`
        `garage = {}`
        `try: exec(recipe, garage)`
        `except: pass`
Looking at the defined method, we can see that the exec() directly executes python code that we provided in recipe variable.
With this, we can craft our own malcious recipe that will be passed to the exec() and executed on the server. 

## Exploit

This exploit script abuses two vulnerabilities, SQL injection and insecure deserialization in the web application. It creates a specially crafted payload using Python's pickle module, which is then serialized, base64 encoded, and appended to a URL parameter during a GET request. The payload, when deserialized on the server side, invokes the os.system method with a command (cat flag.txt > application/static/flag.txt), allowing us to read the contents of the 'flag.txt' file on the server. The script demonstrates exploitation by chaining together two vulnerabilities and retrieving the contents of the exploited file from the target URL.

## More Information

[Pickle - Insecure Deserialization](https://blog.securelayer7.net/insecure-deserialization-attack-in-python-application/)

