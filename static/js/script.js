document.addEventListener("DOMContentLoaded", function () {
  const urlInput = document.getElementById("url-input");
  const submitBtn = document.getElementById("submit-btn");
  const urlForm = document.getElementById("url-form");
  const responseContainer = document.getElementById("response-container");

  function isValidUrl(url) {
    const urlPattern =
      /^(https?:\/\/)?([a-zA-Z\d\-._~%!$&'()*+,;=:]+@)?((([a-zA-Z\d]([a-zA-Z\d-]*[a-zA-Z\d])*\.)+[a-zA-Z]{2,})|(\d{1,3}\.){3}\d{1,3})(:\d{1,5})?(\/[^\s]*)?$/;
    return urlPattern.test(url);
  }

  function validateUrl() {
    const urlValue = urlInput.value;
    const isValid = isValidUrl(urlValue);

    urlInput.classList.toggle("valid", isValid);
    urlInput.classList.toggle("invalid", !isValid);
    submitBtn.disabled = !isValid;
  }

  function handleFormSubmit(event) {
    event.preventDefault();
    const url = urlInput.value;

    if (!isValidUrl(url)) {
      console.error("Invalid URL:", url);
      return;
    }

    fetch("/extract_features", {
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
        displayResponse(data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  function displayResponse(data) {
    responseContainer.innerHTML =
      "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
  }

  urlInput.addEventListener("input", validateUrl);
  urlForm.addEventListener("submit", handleFormSubmit);
});
