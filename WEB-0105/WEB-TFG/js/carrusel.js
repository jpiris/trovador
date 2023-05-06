// Funcionamiento del carrusel
// INDEX, PRODUCTO Y CATEGORÍA

const contenedorProductos = [...document.querySelectorAll('.contenedor-carrusel')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];

contenedorProductos.forEach((item, i) => {
    let dimensionesContenedor = item.getBoundingClientRect();
    let anchoContenedor = dimensionesContenedor.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += anchoContenedor;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= anchoContenedor;
    })
})