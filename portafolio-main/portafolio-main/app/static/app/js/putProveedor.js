function upProveedor () {
    let id_proveedorPut = document.getElementById("id_proveedorPut").value;
    let nombre_proveedorPut = document.getElementById("nombre_proveedorPut").value; 
    let apellido_proveedorPut = document.getElementById("apellido_proveedorPut").value;
    let rut_proveedorPut = document.getElementById("rut_proveedorPut").value;
    let contactoPut = document.getElementById("contactoPut").value;
    
    let ruta = "http://127.0.0.1:8001/api/v1/proveedor/"
    
    let xhr = new XMLHttpRequest();
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
        "id_proveedor":`+`"${id_proveedorPut}"`+`,
        "nombre_proveedor":`+`"${nombre_proveedorPut}"`+`, 
        "apellido_proveedor":`+`"${apellido_proveedorPut}"`+`,
        "rut_proveedor":`+`"${rut_proveedorPut}"`+`,
        "contacto":`+`"${contactoPut}"`+`
    }`;
    console.log(campo)
    
  
    xhr.send(campo);
}


$("#btnActualizarProveedor").click(function() {
    
    upProveedor();
});