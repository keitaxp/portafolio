function uptMesa () {
    let id_mesaPut = document.getElementById("id_mesaPut").value;
    let disponibilidadPut = $('input[name="optDisponEdit"]:checked').val();
    let capacidadPut = document.getElementById("capacidadPut").value;

    let ruta = "http://127.0.0.1:8001/api/v1/mesa/"
    
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
        "id_mesa":`+`"${id_mesaPut}"`+`,
        "disponibilidad":`+`"${disponibilidadPut}"`+`, 
        "capacidad":`+`"${capacidadPut}"`+`
    }`;
    console.log(campo)
    
  
    xhr.send(campo);
}


$("#btnActualizarMesa").click(function() {
    
    uptMesa();
});