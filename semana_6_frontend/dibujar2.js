document.addEventListener('DOMContentLoaded', () => {

    // state
    let dibujando = false;

    // elements
    let puntos = [];
    let lineas = [];
    let svg = null;

    function render() {

        // Crear el área de selección
        svg = d3.select('#dibujo')
                .attr('height', window.innerHeight)
                .attr('width', window.innerWidth);

        svg.on('mousedown', function() {
            dibujando = true;
            const coordenadas = d3.mouse(this);
            dibujar_punto(coordenadas[0], coordenadas[1], false);
        });

        svg.on('mouseup', () =>{
            dibujando = false;
        });

        svg.on('mousemove', function() {
            if (!dibujando)
                return;
            const coordenadas = d3.mouse(this);
            dibujar_punto(coordenadas[0], coordenadas[1], true);
        });

        document.querySelector('#borrar').onclick = () => {
            for (let i = 0; i < puntos.length; i++)
                points[i].remove();
            for (let i = 0; i < lineas.length; i++)
                lines[i].remove();
            puntos = [];
            lineas = [];
        }

    }

    function dibujar_punto(x, y, conectar) {

        const color = document.querySelector('#color-picker').value;
        const grosor = document.querySelector('#grosor-picker').value;

        if (conectar) {
            const ultimo_punto = puntos[puntos.length - 1];
            const linea = svg.append('line')
                            .attr('x1', ultimo_punto.attr('cx'))
                            .attr('y1', ultimo_punto.attr('cy'))
                            .attr('x2', x)
                            .attr('y2', y)
                            .attr('stroke-width', grosor * 2)
                            .style('stroke', color);
            lineas.push(linea);
        }

        const punto = svg.append('circle')
                         .attr('cx', x)
                         .attr('cy', y)
                         .attr('r', grosor)
                         .style('fill', color);
        puntos.push(punto);
    }

    render();
});
