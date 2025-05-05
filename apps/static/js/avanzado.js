document.getElementById("enviarTodo").addEventListener("click", () => {
    const inputs = document.querySelectorAll('[name="respuesta"]');
    const respuestas = [];

    inputs.forEach((input, index) => {
        respuestas.push({
            index: index,
            respuesta: input.value
        });
    });

    fetch("avanzado/api/verificar", {
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
        localStorage.setItem('avanzado', puntos)
        localStorage.setItem("correctas_avance", JSON.stringify(correctas));
        localStorage.setItem("incorrectas_avance", JSON.stringify(incorrectas));
        const currentHost = "";
        Swal.fire({
            title: 'Nombre',
            html: `
              
            `, // Mostrar el host actual justo arriba del campo de entrada
            input: 'text',
            inputLabel: 'Escriba su nombre',
            inputPlaceholder: 'Ejemplo: Juanito',
            inputValue: currentHost !== 'No asignado' ? currentHost : '', // Si hay un host, se muestra como valor inicial
            showCancelButton: true,
            confirmButtonText: 'Guardar',
            preConfirm: (host) => {
              if (!host) {
                Swal.showValidationMessage('El nombre es obligatorio');
              }
              return host;
            }
          }).then((result) => {
            if (result.isConfirmed) {
              const host = result.value;
              // Enviar el valor del host al backend
              let basico = localStorage.getItem('basico')
              let intermedio = localStorage.getItem('intermedio')
              let avanzado = localStorage.getItem('avanzado')
              let correctas_basica  =localStorage.getItem('correctas_basicas')
              let incorrectas_basiva  =localStorage.getItem('incorrectas_basicas')
              let correctas_intermedia  =localStorage.getItem('correctas_intermedias')
              let incorrectas_intermedias  =localStorage.getItem('incorrectas_intermedias')
              let correctas_avance  =localStorage.getItem('correctas_avance')
              let incorrecta_avance  =localStorage.getItem('incorrectas_avance')
              $.ajax({
                url: '/registro/registrar',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ user: host, basico:basico,intermedio:intermedio, avanzado:avanzado,correctas:correctas_basica, incorrectas:incorrectas_basiva, correctas_intermedia: correctas_intermedia, incorrectas_intermedia: incorrectas_intermedias, correctas_avanced:correctas_avance , incorrectas_avanced: incorrecta_avance}),
                success: (response) => {
                  Swal.fire('Éxito', response.message, 'success');
                },
                error: (xhr) => {
                  Swal.fire('Error', xhr.responseJSON.error, 'error');
                }
              });
            }
          });
        
    })
    .catch(err => console.error("Error al verificar respuestas:", err));
});


