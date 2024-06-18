document.addEventListener("DOMContentLoaded", function() {
    var colorButton = document.getElementById("colorButton1");
// Füge einen Klick-Event-Listener zum Button hinzu
    colorButton.addEventListener("click", function() {
// Erstelle ein <input> Element vom Typ "color"
    var colorInput = document.createElement("input");
    colorInput.type = "color";
// Füge einen Event-Listener zum Farbeingabe-Element hinzu
    colorInput.addEventListener("input", function() {
// Setze die Hintergrundfarbe der Seite entsprechend der ausgewählten Farbe
    document.body.style.backgroundColor = colorInput.value;
    });
// Simuliere einen Klick auf das Farbeingabe-Element, um den Farbwähler zu öffnen
    colorInput.click();
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const myForm = document.getElementById("myForm");

    // Füge einen Event-Listener zum Formular hinzu
    myForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Verhindere das Standardverhalten des Formulars (Seitenneuladen)

        // Hole den eingegebenen Text aus dem Input-Feld
        const inputText = myForm.querySelector("input[type='text']").value;

        // Erstelle ein neues <p>-Element
        const newParagraph = document.createElement("div");
        newParagraph.setAttribute("class","posting");
        newParagraph.textContent = inputText; // Setze den Text des <p>-Elements

        // Füge das <p>-Element oberhalb des Formulars ein
        document.getElementById("NewPosts").appendChild(newParagraph);
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const apiKey = '17b62d4c54d46417f60f83e9fd630b56';
    const city = 'Ludwigsburg';
    const weatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=de`;

    fetch(weatherUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      const weatherDiv = document.getElementById('weather');
      const weatherDescription = data.weather[0].description;
      const temperature = data.main.temp;
      weatherDiv.innerHTML = `Das Wetter in ${city}: ${weatherDescription}, ${temperature}°C`;
    })
    .catch(error => {
      console.error('Error fetching weather data:', error);
      const weatherDiv = document.getElementById('weather');
      weatherDiv.innerHTML = 'Wetterdaten konnten nicht geladen werden.';
    });
});


