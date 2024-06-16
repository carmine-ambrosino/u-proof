document.getElementById('submit-btn').addEventListener('click', function(event) {
    event.preventDefault();
    var url = document.getElementById('url-input').value;
    
    fetch('/extract_features', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        var featuresDiv = document.getElementById('response-container');
        featuresDiv.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
