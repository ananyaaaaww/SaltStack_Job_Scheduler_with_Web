    function checkFile() {
        const fileInput = document.getElementById('fileInput');
        const fileError = document.getElementById('fileError');
        const allowedExtensions = /(\.sh)$/i;

        if (!allowedExtensions.exec(fileInput.value)) {
            fileInput.value = '';
            fileError.textContent = 'Please upload .sh format only.';
            return false;
        } else {
            fileError.textContent = '';
        }
    }

    function validateForm() {
        const fileInput = document.getElementById('fileInput');

        // Check if a file is selected
        if (fileInput.value === '') {
            alert('Please select a file.');
            return false;
        }

        // Check file extension
        const allowedExtensions = /(\.sh)$/i;
        if (!allowedExtensions.exec(fileInput.value)) {
            alert('Please upload .sh format only.');
            return false;
        }

        return true;
    }
    function handleResponse(data) {
        // Create a formatted HTML element
        const formattedElement = document.createElement('pre');
        formattedElement.style.color = 'purple';  // Set the color in CSS
        formattedElement.textContent = JSON.stringify(data, null, 4);  // Stringify with indentation
      
        // Append the formatted element to your container in HTML
        const dataContainer = document.getElementById('data-container');
        dataContainer.appendChild(formattedElement);
      }

