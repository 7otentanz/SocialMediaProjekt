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

/* Script für die TomTom API */

document.addEventListener('DOMContentLoaded', function () {
    tt.setProductInfo('sociall', '1.0');
    var map = tt.map({
        key: '5AVUtGYgGWb40iePsDUVZCkVyQjnGbn7',
        container: 'map',
        center: [9.1672737, 48.892372], // Set to your desired coordinates
        zoom: 6
    });

    map.on('style.load', function() {
        // Add Traffic Flow Layer
        map.addLayer({
            id: 'traffic-flow',
            type: 'raster',
            source: {
                type: 'raster',
                tiles: [
                    'https://api.tomtom.com/traffic/map/4/tile/flow/relative/{z}/{x}/{y}.png?key=5AVUtGYgGWb40iePsDUVZCkVyQjnGbn7'
                ],
                tileSize: 256
            }
        });

        // Add Traffic Incidents Layer
        map.addLayer({
            id: 'traffic-incidents',
            type: 'raster',
            source: {
                type: 'raster',
                tiles: [
                    'https://api.tomtom.com/traffic/map/4/tile/incidents/s1/{z}/{x}/{y}.png?key=5AVUtGYgGWb40iePsDUVZCkVyQjnGbn7'
                ],
                tileSize: 256
            }
        });

        // Calculate and Add Route
        calculateRoute();
    });

    function addRouteToMap(coordinates) {
        var routeLayer = {
            id: 'route',
            type: 'line',
            source: {
                type: 'geojson',
                data: {
                    type: 'Feature',
                    geometry: {
                        type: 'LineString',
                        coordinates: coordinates
                    }
                }
            },
            paint: {
                'line-color': '#4a90e2',
                'line-width': 6
            }
        };
        map.addLayer(routeLayer);
    }

    function calculateRoute() {
        var start = '9.1672737,48.892372';
        var end = '8.647264888758022,48.83021071625998';
        var routeUrl = `https://api.tomtom.com/routing/1/calculateRoute/${start}:${end}/json?key=5AVUtGYgGWb40iePsDUVZCkVyQjnGbn7&travelMode=car`;

        fetch(routeUrl)
            .then(response => response.json())
            .then(data => {
                if (data.routes && data.routes.length > 0) {
                    var coordinates = data.routes[0].legs[0].points.map(point => [point.longitude, point.latitude]);
                    addRouteToMap(coordinates);
                } else {
                    console.error('No route found');
                }
            })
            .catch(error => {
                console.error('Error calculating route:', error);
            });
    }
});