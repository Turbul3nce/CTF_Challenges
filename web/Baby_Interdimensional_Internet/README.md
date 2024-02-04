# Python Application | My Exec() Now

## Description

After checking out the website, I notice there is a number that gets randomly generated everytime the page is refreshed. After checking the source code I see a reference to a /debug page. Going here exposed the vulnerable code. 
###
###### `if request.method == 'POST':`
######         `ingredient = request.form.get('ingredient', '')`
######         `recipe = '%s = %s' % (ingredient, request.form.get('measurements', ''))`
###
This part of the source code tells me the measurements in the GET request are stored in recipe, which is later used as a parameter in calc(recipe).  
###### `def calc(recipe):`
######        `global garage`
######        `garage = {}`
######        `try: exec(recipe, garage)`
######        `except: pass`

Looking at the defined method, we can see that the exec() directly executes python code defined in the recipe.
With this, we can craft our own malcious recipe that will be passed to the exec() and executed on the server. 

## framework 

- Flask
  
## Exploit

The detect script makes a POST request to the root route, manipulating custom ingredients and measurements to test identify control over the number through the exec(). The exploit script crafts our payload within the 'measurements' parameter. This payload uses the 'subprocess' module to execute a specified command ('cat flag'). Subsequently, the script sends a second POST request with this payload, triggering the execution of the command on the server. The printed response unveils the output of the executed command, revealing the flag.

## More Information

[Hacking Python Applications](https://medium.com/swlh/hacking-python-applications-5d4cd541b3f1)

