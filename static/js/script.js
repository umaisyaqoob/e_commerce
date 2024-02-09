// Function to show the element
function showElement() {
    document.querySelector('.section-10-cookies-main').style.display = 'flex';
    setTimeout(hideElement, 5000); // Hide after 5 seconds
  }

  // Function to hide the element
  function hideElement() {
    document.querySelector('.section-10-cookies-main').style.display = 'none';
    setTimeout(showElement, 3000); // Show after 3 seconds
  }

  // Initial call to start the cycle
  showElement();