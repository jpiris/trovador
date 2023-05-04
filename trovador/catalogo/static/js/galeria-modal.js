// Funcionamiento de la galeria modal
// articulo.html


var imgGrande = document.getElementById("grande");
var miniatura = document.getElementsByClassName("miniatura");

for (let i = 0; i < miniatura.length; i++){
    
    miniatura[i].addEventListener("click", function(e){
        let src = e.target.src;
        imgGrande.setAttribute("src", src);
    })
    
}