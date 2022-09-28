document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#formulario').onsubmit = () => {

        // Inicializar nueva solicitud
        const solicitud = new XMLHttpRequest();
        const moneda = document.querySelector('#moneda').value;
        solicitud.open('POST', '/convertir');

        // Función a llamar cuando se complete la solicitud
        solicitud.onload = () => {

            // Extraer datos JSON de la solicitud
            const datos = JSON.parse(solicitud.responseText);

            // Actualizamos el div de resultado
            if (datos.exito) {
                const contenido = `1 USD es igual a ${datos.tasa} ${moneda}.`
                document.querySelector('#resultado').innerHTML = contenido;
            }
            else {
                document.querySelector('#resultado').innerHTML = 'Hubo un error.';
            }
        }

        // Agregar datos a enviar con la solicitud
        const datos = new FormData();
        datos.append('moneda', moneda);

        // Enviar solicitud
        solicitud.send(datos);
        return false;
    };

});
