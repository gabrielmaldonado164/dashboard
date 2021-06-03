function message_error(obj){
    let  html = '' 
    if(typeof(obj) == 'object'){
        html = '<ul style="text-align:left; ">';
        $.each(obj, function(key, value ){ //con el metodo each recorro el object,  function recorro la key y el value
            html += '<li>' + key +': '+ value + '</li>';
        });
        html += '</ul>';
    }
    else{
        html = '<p>'+obj+'</p>';
    }

    Swal.fire({
        title:'Error',
        html:html,
        icon:'error'
    });

}


function submit_with_ajax(url, parameters, callback){
    $.confirm({
        theme: 'modern',
        title: 'Confirmación',
        icon: 'fa fa-info',
        content: 'Esta seguro de realizar la siguiente accion?',
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url:url, //window.location.pathname
                        type:'POST',
                        data:parameters,
                        dataType:'json',
                        processData:false,//se usa para el FORM DATA
                        contentType:false, //se usa para el FORM DATA
                   }).done(function(data) {
                       if(!data.hasOwnProperty('error')){//hasOwnProperty -> me deje tomar el dato de la propiedad
                            callback() //para que me puedan pasar una funcion y ejecutar que accion quiero realizar
                            return false;
                       }
                        message_error(data.error);//si hay error lo recorro
                   }).fail(function(jqXHR, textStatus,errorThrown ) {//methods the ajax for errors
                        alert(textStatus+': '+ errorThrown);
                   });
                    
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {
                    
                }
            },
        }
    })

};
