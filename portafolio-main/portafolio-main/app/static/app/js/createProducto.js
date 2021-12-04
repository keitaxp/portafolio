
function saveProducto () {
    let id_proveedor = document.getElementById("id_proveedor").value; 
    let nombre_producto = document.getElementById("nombre_producto").value;
    let descripcion = document.getElementById("descripcion").value;

    let ruta = "http://127.0.0.1:8001/api/v1/producto/"
    
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
        "id_proveedor":`+`"${id_proveedor}"`+`, 
        "nombre_producto":`+`"${nombre_producto}"`+`,
        "descripcion":`+`"${descripcion}"`+`
    }`;
    console.log(campo)
    
  
    xhr.send(campo);
}


$("#btnCrearProducto").click(function() {
    
    saveProducto();
    //cambiar nombre fun
});
