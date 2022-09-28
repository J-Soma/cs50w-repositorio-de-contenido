document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = contar;
});

let contador = 0;

function contar() {
    contador++;
    document.querySelector('#contador').innerHTML = contador;

    if (contador % 10 === 0) {
        alert(`El contador está en ${contador}!`);
    }
}
