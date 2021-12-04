function upProducto () {
    let id_productoPut = document.getElementById("id_productoPut").value;
    let id_proveedorPut = document.getElementById("id_proveedorPut").value; 
    let nombre_productoPut = document.getElementById("nombre_productoPut").value;
    let descripcionPut = document.getElementById("descripcionPut").value;
    
    let ruta = "http://127.0.0.1:8001/api/v1/producto/"
    
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
        "id_producto":`+`"${id_productoPut}"`+`,
        "id_proveedor":`+`${id_proveedorPut}`+`, 
        "nombre_producto":`+`"${nombre_productoPut}"`+`,
        "descripcion":`+`"${descripcionPut}"`+`
    }`;
    console.log(campo)
    
  
    xhr.send(campo);
}


$("#btnActualizarProducto").click(function() {
    
    upProducto();
});