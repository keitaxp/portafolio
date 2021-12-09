let rutaget = "http://127.0.0.1:8001/api/v1/receta/";

function agregarPedidos(id_receta){
    let rutaRecetaPedido = "http://127.0.0.1:8001/api/v1/receta_pedido/";

    

    //Agregar receta a "recetaspedidos"
    var xhr = new XMLHttpRequest();
    xhr.open("POST", rutaRecetaPedido);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status)
            console.log(xhr.responseText);
            if (xhr.status === 200 )
            console.log("receta añadida")
        
            else if (xhr.status != 200 || typeof xhr.status === "undefined" || xhr.status === 400)
            console.log("la receta no se ha podido añadir")
        }
    };

    let recetaPedida = `{
        "id_receta":`+`"${id_receta}"`+`
    }`;   
  
    xhr.send(recetaPedida);
   

}

$.get(rutaget, function(leerRuta){
    let body='';
    let contt = 0;
    let precioTotal = 0;
    leerRuta.forEach(function(params){
        
        contt++;
        precioTotal = precioTotal + params.precio;
        body += `<div class="four columns">
                    <div class="card">
                        <img src="/app/static/app/img/platillo1.jpg" class="imagen-platillo u-full-width">
                        <div class="info-card">
                            <h4>${params.nombre}</h4>
                            <p>${params.descripcion}</p>
                            <img src="/app/static/app/img/estrellas.png">
                            <p> $${params.precio} </p>
                            <button href="#" class="u-full-width button-primary button input agregar-carrito" data-id="1" onclick="agregarPedidos('${params.id_receta}')" id="Receta${contt}">Agregar al carrito</button>
                        </div>
                    </div>
                </div>`
        
    })
    document.getElementById('containerRecetas').innerHTML = body;

    
})

