function uptReserva () {
    let id_reservaPut = document.getElementById("id_reservaPut").value;
    let id_mesaPut = document.getElementById("id_mesaPut").value; 
    let rut_clientePut = document.getElementById("rut_clientePut").value;
    let cantidad_personasPut = document.getElementById("cantidad_personasPut").value;
    let fechaPut = document.getElementById("fechaPut").value;
    

    let ruta = "http://127.0.0.1:8001/api/v1/reserva/"
    
    var xhr = new XMLHttpRequest();
    console.log("1")
    xhr.open("PUT", ruta);
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
        "id_reserva":`+`"${id_reservaPut}"`+`,
        "id_mesa":`+`${id_mesaPut}`+`, 
        "rut_cliente":`+`"${rut_clientePut}"`+`,
        "cantidad_personas":`+`"${cantidad_personasPut}"`+`,
        "fecha":`+`"${fechaPut}"`+`
    }`;
    console.log(campo)
    
  
    xhr.send(campo);
}


$("#btnActualizarReserva").click(function() {
    
    uptReserva();
});