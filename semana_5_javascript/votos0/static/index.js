document.addEventListener('DOMContentLoaded', () => {

    // Conectar al websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Al conectarse, configurar los botones
    socket.on('connect', () => {

        // Cada botón debería emitir un evento "guardar voto"
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                const seleccion = button.dataset.voto;
                socket.emit('guardar voto', {'seleccion': seleccion});
            };
        });
    });

    // Cuando un nuevo voto es anunciado, lo agregamos a la lista desordenada
    socket.on('anunciar voto', dato => {
        const li = document.createElement('li');
        li.innerHTML = `Voto registrado: ${dato.seleccion}`;
        document.querySelector('#votos').append(li);
    });
});
