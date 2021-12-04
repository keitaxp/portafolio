let rutaget = "http://127.0.0.1:8001/api/v1/proveedor/";



$.get(rutaget, function(leerRuta){

    


    let body='';
    let cont = 0;
    leerRuta.forEach(function(params){

        body += `<tr id="rowListareceta"> 

        <td>${params.id_proveedor}</td>
        <td>${params.nombre_proveedor}</td>
        <td>${params.apellido_proveedor}</td>
        <td>${params.rut_proveedor}</td>
        <td>${params.contacto}</td>
        <td>
            <a href="#"><button class="btn btn-primary" id="btnEditar${cont}" onclick="eliminar(${params.id_proveedor})" /i> Borrar </button>
        </td>
        </tr>`
        cont++;
        
      
    })
    document.getElementById('idTbody').innerHTML = body;
})
    
   

    function eliminar(id){
        let rutaDL = "http://127.0.0.1:8001/api/v1/proveedor/" + id;
        let xhr = new XMLHttpRequest();
        console.log("1")
        xhr.open("DELETE", rutaDL);
        xhr.setRequestHeader("Content-Type","application/json");
        console.log("2")
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                console.log(xhr.status)
                console.log(xhr.responseText);
                if (xhr.status === 200)
                console.log("eliminado exitoso")            
                else if (xhr.status != 200 || typeof xhr.status === "undefined" || xhr.status === 400)
                console.log("el registro no se ha podido eliminar")
            }
        };
        console.log("3")
        xhr.send();
    }