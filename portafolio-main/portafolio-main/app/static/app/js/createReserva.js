function savePedido () {
    let id_reserva = document.getElementById("id_reserva").value; 
    let id_mesa = document.getElementById("id_mesa").value;
    let rut_cliente = document.getElementById("rut_cliente").value;
    let cantidad_personas = document.getElementById("cantidad_personas").value;
    let fecha = document.getElementById("fecha").value;


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
        "id_reserva":`+`"${id_reserva}"`+`, 
        "id_mesa":`+`"${id_mesa}"`+`,
        "rut_cliente":`+`"${rut_cliente}"`+`,
        "cantidad_personas":`+`"${cantidad_personas}"`+`,
        "fecha":`+`"${fecha}"`+`
    }`;
    console.log(campo)
    
  
    xhr.send(campo);
}


$("#btnCrearPedido").click(function() {
    
    savePedido();
});