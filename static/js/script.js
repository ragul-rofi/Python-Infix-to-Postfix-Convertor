document.getElementById('calcForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const infixInput = document.getElementById('infix').value;

    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ infix: infixInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.postfix;
    })
    .catch(error => console.error('Error:', error));
});
