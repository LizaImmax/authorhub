// static/script.js

// Sample JavaScript for interactive features

// Function to toggle a hidden element
function toggleElementVisibility(elementId) {
    var element = document.getElementById(elementId);
    if (element.style.display === 'none' || element.style.display === '') {
        element.style.display = 'block';
    } else {
        element.style.display = 'none';
    }
}

// Function to show a notification
function showNotification(message) {
    alert(message);
}

// Function to validate a form
function validateForm() {
    var nameInput = document.getElementById('name');
    var emailInput = document.getElementById('email');

    if (nameInput.value === '' || emailInput.value === '') {
        alert('Please fill in all the required fields.');
        return false;
    }

    return true;
}

// Example: Function to handle AJAX request
function fetchData() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var responseData = JSON.parse(xhr.responseText);
            // Process the data as needed
        }
    };
    xhr.open('GET', 'https://api.example.com/data', true);
    xhr.send();
}

// Add more JavaScript functions as needed for your specific features

