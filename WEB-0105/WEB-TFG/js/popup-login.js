// Funcion para abrir y cerrar los pop up
// LOGIN + REGISTRO

(function() {
    var loginButton = document.getElementById('inicioSesion');
    var closeButton = document.getElementById('cerrar');
    var closeButton2 = document.getElementById('cerrar2');
    var loginDialog = document.getElementById('loginDialog');
    var registroDialog = document.getElementById('registroDialog');
    var registroButton = document.getElementById('registro');

    // Abrir el pop up LOGIN
    loginButton.addEventListener('click', function() {
        loginDialog.showModal();
    });

    // Cerrar el pop up LOGIN
    closeButton.addEventListener('click', function() {
        loginDialog.close();
    });

    // Cambiar a REGISTRO
    registroButton.addEventListener('click', function() {
        loginDialog.close();
        registroDialog.showModal();
    });

    // Cerrar el pop up REGISTRO
    closeButton2.addEventListener('click', function() {
        registroDialog.close();
    });

})();
