// Funcion para abrir y cerrar el pop up
// BÚSQUEDA

(function() {
    var busquedaButton = document.getElementById('busqueda');
    var closeButton4 = document.getElementById('cerrar4');
    var busquedaDialog = document.getElementById('busquedaDialog');

    // Abrir el pop up BUSQUEDA
    busquedaButton.addEventListener('click', function() {
        busquedaDialog.showModal();
    });

    // Cerrar el pop up BUSQUEDA
    closeButton4.addEventListener('click', function() {
        busquedaDialog.close();
    });

})();