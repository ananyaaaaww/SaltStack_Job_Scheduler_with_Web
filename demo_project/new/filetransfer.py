import requests

def filetransfer(file):
    api_url = "http://192.168.64.16:8000/run"
    local_file_path = "/Users/ananya1.intern/Documents/test/" + file
    
# Read the content of the local file
    try:
        with open(local_file_path, "r") as f:
            file_content = f.read()
    except FileNotFoundError:
        print(f"File '{local_file_path}' not found.")
        exit()
    data = {
        "client": "wheel",
        "fun": "file_roots.write",
        "path": "file.sh",  # Specify the path where you want to write the file
        "saltenv": "base",
        "data": file_content,  # Content of the file you want to write
        "username": "ananya",
        "password": "bing",
        "eauth": "pam"
    }
    
    response = requests.post(api_url, json=data)
    return response.json()["return"]

# Call the function
result = filetransfer()
print(result)  # or do something with the result
