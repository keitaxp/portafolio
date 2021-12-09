function savePedido () {
    let id_pedido = document.getElementById("id_pedido").value; 
    let id_mesa = document.getElementById("id_mesa").value;
    let fecha_pedido = document.getElementById("fecha_pedido").value;
    let precio_total = document.getElementById("precio_total").value;

    let ruta = "http://127.0.0.1:8001/api/v1/pedido/"
    
    var xhr = new XMLHttpRequest();
    console.log("1")
    xhr.open("POST", ruta);
    xhr.setRequestHeader("Content-Type", "application/json");
    console.log("2")
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            console.log(xhr.status)
            console.log(xhr.responseText);
            if (xhr.status === 200 )
            console.log("guardado exitoso")
        
            else if (xhr.status != 200 || typeof xhr.status === "undefined" || xhr.status === 400)
            console.log("el guardado no se ha podido realizar")
        }
    };
    console.log("1")
    let campo = `{
        "id_pedido":`+`"${id_pedido}"`+`, 
        "id_mesa":`+`"${id_mesa}"`+`,
        "fecha_pedido":`+`"${fecha_pedido}"`+`,
        "precio_total":`+`"${precio_total}"`+`
    }`;
    console.log(campo)
    
  
    xhr.send(campo);
}


$("#btnCrearPedido").click(function() {
    
    savePedido();
});