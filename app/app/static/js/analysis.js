const api_prediction = "/api/v1/predict"

document.addEventListener("DOMContentLoaded", function () {
  const resultsContainer = document.getElementById("results-container");
  const loadingElement = document.getElementById("loading");
  const url = sessionStorage.getItem("url");

  if (url) {
    fetchPrediction(url)
      .then(data => {
        setTimeout(() => {
          loadingElement.style.display = "none";
          resultsContainer.style.display = "block";

          displayUrl(resultsContainer, data.url);
          displayPrediction(resultsContainer, data.prediction, data.proba);
          displayMotivation(resultsContainer, data.motivation);
        }, 1500); // Wait 150ms
      })
      .catch(error => {
        displayError(loadingElement, "⚠️ URL error", error);
      });
  } else {
    displayError(loadingElement, "⚠️ No URL provided");
  }
});

async function fetchPrediction(url) {
  const response = await fetch(api_prediction, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url: url }),
  });
  if (!response.ok) {
    throw new Error("Network response was not ok");
  }
  return await response.json();
}

function displayPrediction(container, prediction, proba) {
  if (prediction && proba) {
    const progressContainer = document.createElement("div");
    progressContainer.className = "progress-container";

    const progressBar = document.createElement("div");
    progressBar.className = "progress";

    const progressTitle = document.createElement("div");
    progressTitle.className = "progress-title";
    progressTitle.textContent = `${prediction}`;
    progressContainer.appendChild(progressTitle);

    const progressBarFill = document.createElement("div");
    progressBarFill.className = "progress-bar";
    progressBarFill.id = `progress-bar-${prediction}`;
    progressBarFill.style.width = `${proba}%`;

    const percentage = proba.toString().substring(0, 5);
    progressBarFill.textContent = `${percentage}%`;
    progressBar.appendChild(progressBarFill);

    progressContainer.appendChild(progressBar);
    container.appendChild(progressContainer);
  }
}

function displayUrl(container, url) {
  if (url) {
    const urlFieldElement = document.createElement("div");
    urlFieldElement.className = "result-field";
    urlFieldElement.id = "rf-url";

    const urlFieldValue = document.createTextNode(url);
    urlFieldElement.appendChild(urlFieldValue);

    container.appendChild(urlFieldElement);
  }
}

function displayMotivation(container, motivation) {
  if (motivation) {
    const motivationContainer = document.createElement("div");
    motivationContainer.className = "motivation-container";

    const motivationTitle = document.createElement("h3");
    motivationTitle.id = "motivation-title";
    motivationTitle.textContent = "Motivation";
    motivationContainer.appendChild(motivationTitle);

    const motivationContent = document.createElement("ul");
    motivationContent.id = "motivation-text";

    appendMotivationContent(motivationContent, motivation);

    motivationContainer.appendChild(motivationContent);
    container.appendChild(motivationContainer);
  }
}

function appendMotivationContent(container, motivation) {
  if (typeof motivation === 'object' && !Array.isArray(motivation)) {
    for (const [key, value] of Object.entries(motivation)) {
      const listItem = document.createElement("li");

      // Create a span for the key in bold
      const keySpan = document.createElement("span");
      keySpan.className = "motivation-key";
      keySpan.textContent = `${key}: `;

      // Create a span for the value
      const valueSpan = document.createElement("span");
      valueSpan.className = "motivation-value";

      if (typeof value === 'object') {
        // Recursively append nested objects
        const nestedList = document.createElement("ul");
        appendMotivationContent(nestedList, value);
        valueSpan.appendChild(nestedList);
      } else {
        valueSpan.textContent = value;
      }

      listItem.appendChild(keySpan);
      listItem.appendChild(valueSpan);
      container.appendChild(listItem);
    }
  } else {
    const listItem = document.createElement("li");
    listItem.textContent = motivation;
    container.appendChild(listItem);
  }
}

function displayError(element, message, error = null) {
  element.textContent = message;
  if (error) {
    console.error("Error:", error);
  }
}
