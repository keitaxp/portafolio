function uptBodega () {
    let id_bodegaPut = document.getElementById("id_bodegaPut").value;
    let id_productoPut = document.getElementById("id_productoPut").value; 
    let stockPut = document.getElementById("stockPut").value;
    

    let ruta = "http://127.0.0.1:8001/api/v1/bodega/"
    
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
        "id_bodega":`+`"${id_bodegaPut}"`+`,
        "id_producto":`+`${id_productoPut}`+`, 
        "stock":`+`"${stockPut}"`+`
    }`;
    console.log(campo)
    
  
    xhr.send(campo);
}


$("#btnActualizarBodega").click(function() {
    
    uptBodega();
});