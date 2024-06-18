document.addEventListener("DOMContentLoaded", function () {
  const urlInput = document.getElementById("url-input");
  const submitBtn = document.getElementById("submit-btn");
  const urlForm = document.getElementById("url-form");

  // function isValidUrl(url) {
  //   const urlPattern =
  //     /^(https?:\/\/)?([a-zA-Z\d\-._~%!$&'()*+,;=:]+@)?((([a-zA-Z\d]([a-zA-Z\d-]*[a-zA-Z\d])*\.)+[a-zA-Z]{2,})|(\d{1,3}\.){3}\d{1,3})(:\d{1,5})?(\/[^\s]*)?$/;
  //   return urlPattern.test(url);
  // }

  
  function isValidUrl(url) {
    const urlPattern = new RegExp(
      "^(https?:\\/\\/)?" + // protocol
      "((([a-zA-Z\\d]([a-zA-Z\\d-]*[a-zA-Z\\d])*)\\.)+[a-zA-Z]{2,}|" + // domain name
      "((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
      "(\\:\\d+)?(\\/[-a-zA-Z\\d%_.~+]*)*" + // port and path
      "(\\?[;&a-zA-Z\\d%_.~+=-]*)?" + // query string
      "(\\#[-a-zA-Z\\d_]*)?$", "i"
    );
    return !!urlPattern.test(url);
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

    sessionStorage.setItem('url', url);
    window.location.href = '/api/v1/url';
  }

  urlInput.addEventListener("input", validateUrl);
  urlForm.addEventListener("submit", handleFormSubmit);
});
