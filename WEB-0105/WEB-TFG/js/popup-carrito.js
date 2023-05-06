// Funcion para abrir y cerrar el pop up
// CARRITO

(function() {
    var carritoButton = document.getElementById('carritoCompra');
    var closeButton3 = document.getElementById('cerrar3');
    var carritoDialog = document.getElementById('carritoDialog');
    var carritoCompleto = document.getElementById('carrito-completo');
    var comprar = document.getElementById('comprar');

    // Abrir el pop up LOGIN
    carritoButton.addEventListener('click', function() {
        carritoDialog.showModal();
    });

    // Cerrar el pop up LOGIN
    closeButton3.addEventListener('click', function() {
        carritoDialog.close();
    });

})();