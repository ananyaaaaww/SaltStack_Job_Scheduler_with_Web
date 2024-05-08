import requests

def salt_key():
    api_url = "http://192.168.64.16:8000/run"
    
    data = {
        "client": "local",
        "tgt": "*", 
        "fun": "test.ping",
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    }
    
    response = requests.post(api_url, json=data)
    data= response.json()["return"]
    data1=data[0]
    keys = [key.strip() for key in data1.keys()]
    return keys

# Call the function
result = salt_key()
print(result) 