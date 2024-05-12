
async function getTestPing() {
    const response = await fetch("http://192.168.64.16:8000/run", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            "client": "local",
            "tgt": "*", 
            "fun": "test.ping",
            "username": "ananya",
            "password": "bing",
            "eauth": "pam"
        })
    })
    if (!response.ok) {
        throw new Error(`API request failed: ${response.status}`);
    }

    var data = await response.json()['return'][0];
    var keys = Object.keys(data)
    // console.log(data)

    const ddMenu = document.getElementById("ddown");
    ddMenu.innerHTML = ""; // Clear existing options

    for(const key of keys) {
        const option = document.createElement("option")
        option.value = key
        option.text = key
        ddMenu.appendChild(option)
    }
}

getTestPing()