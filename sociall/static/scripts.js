// Wenn auf den Button geklickt wird, wird Dropdownliste angezeigt
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Wenn außerhalb des Buttons geklickt wird, wird Dropdownliste ausgeblendet
window.onclick = function(event) {
if (!event.target.matches('.dropbtn')) {
var dropdowns = document.getElementsByClassName("dropdown-content");
var i;
for (i = 0; i < dropdowns.length; i++) {
var openDropdown = dropdowns[i];
if (openDropdown.classList.contains('show')) {
    openDropdown.classList.remove('show');
    }
}
}
}

/* Script für Wetter-API */
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

/* Script für die mapbox API */
