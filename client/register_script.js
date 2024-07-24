function getInputValues() {
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;


    fetch('http://localhost:5000/api/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, password: password })
    })
    .then(response => {
        if (!response.ok) {
            alert("something went wrong");
        }
        return response.json();
    })
    .then(data => {
        window.alert(JSON.stringify(data));
    })
    .catch((error) => {
        window.alert(error);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.login-container form').addEventListener('submit', function(event) {
        event.preventDefault(); 
        getInputValues();
    });
});
