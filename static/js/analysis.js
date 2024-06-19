document.addEventListener("DOMContentLoaded", function () {
  const resultsContainer = document.getElementById("results-container");
  const loadingElement = document.getElementById("loading");
  const url = sessionStorage.getItem("url");

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
        // Add wait 150 ms to show prediction
        setTimeout(() => {
          loadingElement.style.display = "none";
          resultsContainer.style.display = "block";

          // Bar block
          if (data.prediction && data.prediction_proba) {
            const progressContainer = document.createElement("div");
            progressContainer.className = "progress-container";

            const progressBar = document.createElement("div");
            progressBar.className = "progress";

            const progressTitle = document.createElement("div");
            progressTitle.className = "progress-title";
            progressTitle.textContent = `${data.prediction}`;
            progressContainer.appendChild(progressTitle);

            const progressBarFill = document.createElement("div");
            progressBarFill.className = "progress-bar";
            progressBarFill.id = `progress-bar-${data.prediction}`;
            progressBarFill.style.width = `${data.prediction_proba}%`;

            precentage = data.prediction_proba.toString().substring(0, 5);
            progressBarFill.textContent = `${precentage}%`;
            progressBar.appendChild(progressBarFill);

            progressContainer.appendChild(progressBar);
            resultsContainer.appendChild(progressContainer);
          }

          // Url block
          if (data.url) {
            const urlFieldElement = document.createElement("div");
            urlFieldElement.className = "result-field";
            urlFieldElement.id = "rf-url";

            const urlFieldValue = document.createTextNode(data.url);
            urlFieldElement.appendChild(urlFieldValue);

            resultsContainer.appendChild(urlFieldElement);
          }


        }, 150); // Wait 150ms
      })
      .catch((error) => {
        loadingElement.textContent = "⚠️ URL error";
        console.error("Error:", error);
      });
  } else {
    loadingElement.textContent = "⚠️ No URL provided";
  }
});
