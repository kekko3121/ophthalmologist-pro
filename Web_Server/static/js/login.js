//Validation Code for input field form

//variables to store form data
const username = document.querySelector('#username');
const password = document.querySelector('#password');
const remember = document.querySelector('#remember');
const submit = document.querySelector("#submit");
const errorMessage = document.querySelector('#error-message');

//interacts with the click event of the login button
submit.addEventListener('click', (event) => {
    event.preventDefault();

    let isValid = true; //fuction for verify data form

    //Username Validation
    if(username.value.trim() == ''){
        error(username, '#username_error', "Please fill up your Username");

        isValid = false;
    }

    //password Validation
    if(password.value.trim() == ''){
        error(password, '#pass_error', "Please fill up your password");

        isValid = false;
    }

    // Check if isValid is still true
    if (isValid) {
        // If there are no errors, submit the form
        sendDataToFlask();
    }
});

function error(element, id, errorMessage){
    // Update the visual style of the form element to indicate an error
    element.style.border = '2px red solid';
    // Find the parent element of the form element
    const parent = element.parentElement;
   // Select the error message container using the provided CSS selector
   const errorContainer = parent.querySelector(id);
   // Display the error message container
   errorContainer.style.display = 'block';
   // Set the error message text
   errorContainer.textContent = errorMessage;
}


// send the form date to flask
function sendDataToFlask() {
    const formData = new FormData();
    formData.append('username', username.value);
    formData.append('password', password.value);
    formData.append('remember', remember.checked);

    fetch('/login', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from Flask if needed
        console.log(data);

        // Check if there is an error message
        if (data.error) {
            error(errorMessage, '#error-message', data.error)
        }

        //Load the page returned by Flask
        if (data.redirect) {
            window.location.href = data.redirect;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}