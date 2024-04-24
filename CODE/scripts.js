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


