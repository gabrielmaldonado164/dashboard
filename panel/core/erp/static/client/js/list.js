let tblClient
function getData(){
    tblClient = $('#data').DataTable({
        responsive:true,
        autoWidth: false,
        destroy:true,
        deferRender:true, 
        ajax: {
            url:window.location.pathname,
            type:"POST",
            data:{
                "action":"searchdata"
            },
            dataSrc:""
        },
        columns: [ //generro los datos de las columnas que tengo
        {"data":"id"},
        {"data":"names"},
        {"data":"surnames"},
        {"data":"address"},
        {"data":"id"},

        ],
        columnDefs:[ //edit la ultima columna para agregar botones
            {
                targets: [4],
                class: 'text-center',
                ordenable:false,
                render: function(data, type, row){ //puede rendear cualquier contenido que quiera a la columba que le diga en este caso los botones
                    let buttons = '<a href= "#" class="btn btn-warning btn-xs" id="btn-edit" ><i class="far fa-edit"></i></a>';
                    buttons +='<a href="#" type="button" class="btn btn-danger btn-xs" id="btn-delete"><i class="fas fa-trash"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function(settings, json){//cuando este completo la carga puedo agregar alguna accion para hacer
            //alert('cargado')
        }
    });

}

$(function() {

    modal_title = $('.modal-title');
    getData();

    $("#btnAdd").on('click', function(){
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Creación de un cliente');
        modal_title.find('i').removeClass().addClass('fas fa-plus');  
        $('form')[0].reset(); //primera posicion del form para saber con cual estoy trabajando
        $('#myModalClient').modal('show'); //muestra el modal
    });

    $('#data tbody')
        .on('click','#btn-edit', function(){ // en el body del data busco el id del btn para realizar una funcion cuando lo clickeo
            let tr = tblClient.cell($(this).closest('td,li')).index();// de esta manera llamo los componentes de la columna tanto cuando esta modo completo como modo celular(tamaño), esto es pq cuando cambia el tamaño se crea otros datos de una tabla con la etiqueta "li"
            let data = tblClient.row(tr.row).data() //busco el objeto para que me traiga los datos de la fila

            modal_title.find('span').html('Edicion de un cliente');
            modal_title.find('i').removeClass().addClass('fas fa-edit'); 

            //recupero los datos de los inputs para pode editarlos
            $('input[name="action"]').val('edit');
            $('input[name="id"]').val(data.id);
            $('input[name="names"]').val(data.names);
            $('input[name="surnames"]').val(data.surnames);
            $('input[name="address"]').val(data.address);
            $('#myModalClient').modal('show'); //muestra el modal

        })
        .on('click','#btn-delete', function(){ // en el body del data busco el id del btn para realizar una funcion cuando lo clickeo
            let tr = tblClient.cell($(this).closest('td,li')).index();// de esta manera llamo los componentes de la columna tanto cuando esta modo completo como modo celular(tamaño), esto es pq cuando cambia el tamaño se crea otros datos de una tabla con la etiqueta "li"
            let data = tblClient.row(tr.row).data() //busco el objeto para que me traiga los datos de la fila
            console.log(data);
            let parameters= new FormData(); //-> me permite tener todo los datos incluido FILES
            parameters.append('action','delete');
            parameters.append('id',data.id);
            submit_with_ajax(window.location.pathname, parameters, function(){
                //location.reload();  para recargar una vez ejecutado el proceso
                $('#myModalClient').modal('hide'); //cierra el modal
                tblClient.ajax.reload();
                //getData();//recargar el datatable solamente
    
            });
                

    
        });

    $('#form-create').on('submit', function (e){
        e.preventDefault();//no se haga el envio de manera automatica
        //let parameters = $(this).serializeArray(); ->  me permite tomar todo los datos de mi form como diccionario menos los FILES
        let parameters= new FormData(this); //-> me permite tener todo los datos incluido FILES
        parameters.forEach(function(value,key){
            console.log(key+':'+value);
        });
        console.log(parameters)
        submit_with_ajax(window.location.pathname, parameters, function(){
            //location.reload();  para recargar una vez ejecutado el proceso
            $('#myModalClient').modal('hide'); //cierra el modal
            tblClient.ajax.reload();
            //getData();//recargar el datatable solamente

        });
            
    });
});