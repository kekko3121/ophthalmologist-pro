//Validation Code for input field form

//variables to store form data
const username = document.querySelector('#username');
const password = document.querySelector('#password');
const remember = document.querySelector('#remember');
const submit = document.querySelector("#submit");

//interacts with the click event of the login button
submit.addEventListener('click', (event) => {
    event.preventDefault();

    let isValid = true; //fuction for verify data form

    //Username Validation
    if(username.value.trim() == ''){
        error(username, '#username_error');

        isValid = false;
    }

    //password Validation
    if(password.value.trim() == ''){
        error(password, '#pass_error');

        isValid = false;
    }

    // Check if isValid is still true
    if (isValid) {
        // If there are no errors, submit the form
        sendDataToFlask();
    }
});

function error(element, message){
    // Update the visual style of the form element to indicate an error
    element.style.border = '2px red solid';
    // Find the parent element of the form element
    const parent = element.parentElement;
    // Select the error message container using the provided CSS selector
    const username_error = parent.querySelector(message);
    // Display the error message container
    username_error.style.display = 'block';
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

        //Load the page returned by Flask
        if (data.redirect) {
            window.location.href = data.redirect;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}