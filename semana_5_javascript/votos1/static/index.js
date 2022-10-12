document.addEventListener('DOMContentLoaded', () => {

    // Conectar al websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Al conectar, configurar los botones
    socket.on('connect', () => {

        // Cada botón debería emitir un evento "guardar voto"
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                const seleccion = button.dataset.voto;
                socket.emit('guardar voto', {'seleccion': seleccion});
            };
        });
    });

    // Cuando un nuevo voto es anunciado, agregarlo a la lista desordenada
    socket.on('total votos', datos => {
        document.querySelector('#si').innerHTML = datos.si;
        document.querySelector('#no').innerHTML = datos.no;
        document.querySelector('#talvez').innerHTML = datos["talvez"];
    });
});
