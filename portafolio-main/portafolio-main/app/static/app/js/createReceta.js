
function saveReceta () {
    let precio = document.getElementById("precio").value; 
    let nombre = document.getElementById("nombre").value;
    let descripcion = document.getElementById("descripcion").value;

    let ruta = "http://127.0.0.1:8001/api/v1/receta/"
    
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
        "precio":`+`"${precio}"`+`, 
        "nombre":`+`"${nombre}"`+`,
        "descripcion":`+`"${descripcion}"`+`
    }`;
    console.log(campo)
    
  
    xhr.send(campo);
}


$("#btnCrearReceta").click(function() {
    
    saveReceta();
});
