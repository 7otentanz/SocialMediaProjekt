<div id="particles-js"></div>
<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  document.addEventListener('DOMContentLoaded', function () {
    particlesJS('particles-js', {
      particles: {
        number: {
          value: 100,
          density: {
            enable: true,
            value_area: 800
          }
        },
        color: {
          value: "#ffffff"
        },
        shape: {
          type: "circle",
          stroke: {
            width: 0,
            color: "#000000"
          },
          polygon: {
            nb_sides: 5
          },
          image: {
            src: "img/github.svg",
            width: 100,
            height: 100
          }
        },
        opacity: {
          value: 0.5,
          random: false,
          anim: {
            enable: false,
            speed: 1,
            opacity_min: 0.1,
            sync: false
          }
        },
        size: {
          value: 3,
          random: true,
          anim: {
            enable: false,
            speed: 40,
            size_min: 0.1,
            sync: false
          }
        },
        line_linked: {
          enable: true,
          distance: 150,
          color: "#ffffff",
          opacity: 0.4,
          width: 1
        },
        move: {
          enable: true,
          speed: 6,
          direction: "none",
          random: false,
          straight: false,
          out_mode: "out",
          bounce: false,
          attract: {
            enable: false,
            rotateX: 600,
            rotateY: 1200
          }
        }
      },
      interactivity: {
        detect_on: "canvas",
        events: {
          onhover: {
            enable: true,
            mode: "repulse"
          },
          onclick: {
            enable: true,
            mode: "push"
          },
          resize: true
        },
        modes: {
          grab: {
            distance: 400,
            line_linked: {
              opacity: 1
            }
          },
          bubble: {
            distance: 400,
            size: 40,
            duration: 2,
            opacity: 8,
            speed: 3
          },
          repulse: {
            distance: 200,
            duration: 0.4
          },
          push: {
            particles_nb: 4
          },
          remove: {
            particles_nb: 2
          }
        }
      },
      retina_detect: true
    })
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


