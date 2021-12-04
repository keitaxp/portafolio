
function saveProveedor () {
    let nombre_proveedor = document.getElementById("nombre_proveedor").value; 
    let apellido_proveedor = document.getElementById("apellido_proveedor").value;
    let rut_proveedor = document.getElementById("rut_proveedor").value;
    let contacto = document.getElementById("contacto").value;

    let ruta = "http://127.0.0.1:8001/api/v1/proveedor/"
    
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
        "nombre_proveedor":`+`"${nombre_proveedor}"`+`, 
        "apellido_proveedor":`+`"${apellido_proveedor}"`+`,
        "rut_proveedor":`+`"${rut_proveedor}"`+`,
        "contacto":`+`"${contacto}"`+`
    }`;
    console.log(campo)
    
  
    xhr.send(campo);
}


$("#btnCrearProveedor").click(function() {
    
    saveProveedor();
    //cambiar nombre fun
});
