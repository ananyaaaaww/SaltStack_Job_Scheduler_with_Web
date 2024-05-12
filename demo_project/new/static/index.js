
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

    const data = await response.json();
    console.log(data['return'][0])

    // const ddMenu = document.getElementById("dropDownMenu");
    // ddMenu.innerHTML = ""; // Clear existing options

}

getTestPing()