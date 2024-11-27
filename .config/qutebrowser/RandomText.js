document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript loaded");

  async function displayRandomText() {
    try {
      const response = await fetch('/home/simon/Documents/Vault/splashes.md');
      const text = await response.text();
      const lines = text.split('\n').filter(line => line.trim() !== '');
      const randomLine = lines[Math.floor(Math.random() * lines.length)];
      document.getElementById("randomText").textContent = randomLine;
    } catch (error) {
      console.error("Error fetching text file:", error);
      document.getElementById('randomText').textContent = "Error loading text.";
    }
  }

  // Call the function to display the random text
  displayRandomText();
});

