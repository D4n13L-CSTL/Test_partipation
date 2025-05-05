document.getElementById("enviarTodo").addEventListener("click", () => {
    const inputs = document.querySelectorAll('[name="respuesta"]');
    const respuestas = [];

    inputs.forEach((input, index) => {
        respuestas.push({
            index: index,
            respuesta: input.value
        });
    });

    fetch("basico/api/verificar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(respuestas)
    })
    .then(res => res.json())
    .then(resultados => {
        console.log("Resultados:", resultados);
        let puntos = 0;
        const correctas = [];
        const incorrectas = [];

        resultados.forEach(r => {
            if (r.correcto === true) {
                
                puntos += 2;
                correctas.push({
                    index: r.index,
                    respuesta: respuestas[r.index].respuesta
                });
            } else if (r.correcto === false) {
                incorrectas.push({
                    index: r.index,
                    respuesta: respuestas[r.index].respuesta
                });
            } else {
                console.log(`⚠️ Pregunta ${r.index + 1}: ${r.error}`);
            }
           
        });
        
        localStorage.setItem('basico', puntos)
        localStorage.setItem("correctas_basicas", JSON.stringify(correctas));
        localStorage.setItem("incorrectas_basicas", JSON.stringify(incorrectas));


        window.location.href = "/inter"
    })
    .catch(err => console.error("Error al verificar respuestas:", err));
});
