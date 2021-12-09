let rutagetRP = "http://127.0.0.1:8001/api/v1/receta_pedido/";
let bsRc = "http://127.0.0.1:8001/api/v1/receta/";
$.get(rutagetRP, function(leerRuta){
    $.get(bsRc, function(rc){    

    function buscarReceta(idReceta){
        let datos = new Array();
        rc.forEach(function(params){
            if(params.id_receta == idReceta){
                datos.push({
                    0: params.nombre,
                    1: params.precio
                })
               
            }  
        })
        return datos;
    } 



    let body='';
    let contt = 0;
    let precioTotal = 0;
    let acumNombre = new Array();
    // buscarReceta(params.id_receta_id)[0][0] --->nombre
    // buscarReceta(params.id_receta_id)[0][1] --->precio
    leerRuta.forEach(function(params){
        
        contt++;
        
        precioTotal = precioTotal + buscarReceta(params.id_receta_id)[0][1];
        acumNombre.push(buscarReceta(params.id_receta_id)[0][1]);
        body += `<tr id=""> 
                <td>${buscarReceta(params.id_receta_id)[0][0]}</td> 
                <td>${buscarReceta(params.id_receta_id)[0][1]}</td>               
                </tr>`
        
        
    })
    document.getElementById('tBodyCarritouwu').innerHTML = body;
    acumNombre
    console.log(cantidadTotal(acumNombre) + " - " + precioTotal);


    
    $("#AgregarPedido").click(function(e) {
        agregarPedido(cantidadTotal(acumNombre), precioTotal);
    });

})
})

function agregarPedido(cantidad, precioTotal){
    let fecha = fechaActual();

    let rutaPedido = "http://127.0.0.1:8001/api/v1/pedido/";
    //Agregar receta a "pedido"
    let xhr = new XMLHttpRequest();
    xhr.open("POST", rutaPedido);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status)
            console.log(xhr.responseText);
            if (xhr.status === 200 )
            console.log("pedido añadido")
        
            else if (xhr.status != 200 || typeof xhr.status === "undefined" || xhr.status === 400)
            console.log("el pedido no se ha podido añadir")
        }
    };

    let pedido = `{
        "id_mesa":`+`"1"`+`,
        "fecha_pedido":`+`"${fecha}"`+`,
        "precio_total":`+`"${precioTotal}"`+`,
        "cantidad":`+`"${cantidad}"`+`
    }`;   
  
    xhr.send(pedido);


}

function fechaActual(){
    const fecha = new Date();
    let day = fecha.getDate();
    let month = fecha.getMonth() + 1;
    let anno = fecha.getFullYear();
    return anno + "-" + month + "-" + day;

}

function cantidadTotal(nombre){
    let contador = 0;
    for (let index = 0; index < nombre.length; index++) {
        contador++
    }
    return contador;
}

function vaciarCarrito(){
    let rutagetRP = "http://127.0.0.1:8001/api/v1/receta_pedido/";
    $.get(rutagetRP, function(leerRuta){
        leerRuta.forEach(function(params){
        let pedidoElim = "http://127.0.0.1:8001/api/v1/receta_pedido/" + params.id_receta_pedido;
        let xhr = new XMLHttpRequest();
        xhr.open("DELETE", pedidoElim);
        xhr.setRequestHeader("Content-Type","application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                console.log(xhr.status)
                console.log(xhr.responseText);
                if (xhr.status === 200)
                console.log("pedidos eliminados exitosamente")            
                else if (xhr.status != 200 || typeof xhr.status === "undefined" || xhr.status === 400)
                console.log("los pedidos no se han podido eliminar")
            }
        };
        xhr.send();

        })
    })
}







