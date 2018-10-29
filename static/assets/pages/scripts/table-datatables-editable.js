function load_user_data() {
     var table = $('#sample_editable_1');
     var oTable = table.dataTable({
        "destroy": true,
        "ajax": "/show-user-data/",
        "columns": [
            { "data": "first_name" },
            { "data": "last_name" },
            { "data": "email" },
            { "data": "city" },
            { "data": "action" },
        ],
     });
}

 function open_modal(id){
        $.ajax({
            type: 'GET',
            url: '/open-modal/',
            data: {'id': id},
            success: function(response){
                $('#first_name').val(response.first_name);
                $('#last_name').val(response.last_name);
                $('#email').val(response.email);
                $('#address').val(response.address);
                $('#city').val(response.city);
                $('#country').val(response.country);
                $('#data_id').val(id);
            },
            error: function(){
                alert('error');
            },
            complete: function(){
                $('#add_user').modal('show');
            }
        });
     }

$(document).ready(function() {
    load_user_data();
});
