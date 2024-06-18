document.addEventListener("DOMContentLoaded", function () {
    const resultsContainer = document.getElementById('results-container');
    const loadingElement = document.getElementById('loading');
    const url = sessionStorage.getItem('url');

    if (url) {
        fetch("/api/v1/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ url: url }),
        })
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((data) => {
            //Add a 1s wait before showing the data
            setTimeout(() => {
                loadingElement.style.display = 'none';
                resultsContainer.style.display = 'block';

                const fieldsToShow = ['url','prediction', 'prediction_proba']; 
                fieldsToShow.forEach(field => {
                    if (data[field]) {

                        if (field === 'prediction_proba' && typeof data[field] === 'object') {
                            
                            // Search Max value field
                            const subFields = data[field];
                            const maxField = Object.keys(subFields).reduce((a, b) => subFields[a] > subFields[b] ? a : b);

                            const fieldElement = document.createElement('div');
                            fieldElement.className = 'result-field';

                            const fieldName = document.createElement('strong');
                            fieldName.textContent = `Prob ${maxField}: `;
                            fieldElement.appendChild(fieldName);

                            const fieldValue = document.createTextNode(subFields[maxField]);
                            fieldElement.appendChild(fieldValue);

                            resultsContainer.appendChild(fieldElement);
                        }


                        const fieldElement = document.createElement('div');
                        fieldElement.className = 'result-field';
                        
                        // const fieldName = document.createElement('strong');
                        // fieldName.textContent = `${field}: `;
                        // fieldElement.appendChild(fieldName);
                        
                        const fieldValue = document.createTextNode(data[field]);
                        fieldElement.appendChild(fieldValue);
                        
                        resultsContainer.appendChild(fieldElement);
                    }
                });
            }, 150); // Wait 100ms)
        })
        .catch((error) => {
            loadingElement.textContent = "Error loading data";
            console.error("Error:", error);
        });
    } else {
        loadingElement.textContent = "No URL provided";
    }
});