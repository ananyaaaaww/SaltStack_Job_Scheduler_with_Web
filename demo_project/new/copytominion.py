import requests

def copytominion(target):
    api_url = "http://192.168.64.16:8000/run"
    
# Read the content of the local file

    data = {
        "client": "local",
        "fun": "cp.get_file",
        "tgt": target,  # Target minions or minion group. Use '*' for all minions.
        "arg": [ "salt://file.sh" , "/home/ubuntu/test/second.sh"
        ], 
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    }
    
    response = requests.post(api_url, json=data)
    return response.json()["return"]

# Call the function
# result = copytominion()
# print(result)  # or do something with the result