function getRandomFact() {
    fetch('http://127.0.0.1:5001/randomfact', {
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('fact-text').innerText = data;
    })
    .catch(error => {
        console.error('Error fetching random fact:', error);
        document.getElementById('fact-text').innerText = 'Failed to fetch random fact. Please try again later.';
    });
}

window.addEventListener('DOMContentLoaded', getRandomFact);
