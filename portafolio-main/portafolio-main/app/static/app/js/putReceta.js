function uptReceta () {
    let id_recetaPut = document.getElementById("id_recetaPut").value;
    let precioPut = document.getElementById("precioPut").value; 
    let nombrePut = document.getElementById("nombrePut").value;
    let descripcionPut = document.getElementById("descripcionPut").value;

    let ruta = "http://127.0.0.1:8001/api/v1/receta/"
    
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
        "id_receta":`+`"${id_recetaPut}"`+`,
        "precio":`+`${precioPut}`+`, 
        "nombre":`+`"${nombrePut}"`+`,
        "descripcion":`+`"${descripcionPut}"`+`
    }`;
    console.log(campo)
    
  
    xhr.send(campo);
}


$("#btnActualizarReceta").click(function() {
    
    uptReceta();
});