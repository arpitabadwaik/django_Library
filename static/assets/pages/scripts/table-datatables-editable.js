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
    $('.show_error').removeClass('has-error').addClass('has-success');
    $('#lable_email').hide();
    $('#email').hide();
    $('#div_password').hide();
    $('#div_repassword').hide();

    $.ajax({
        type: 'GET',
        url: '/open-modal/',
        data: {'id': id},
        success: function(response){
            $('#first_name').val(response.first_name);
            $('#last_name').val(response.last_name);
            $('#email').val(response.email);
            $('#password').val(response.password);
            $('#repassword').val(response.password);
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

$('#save_user_data').click(function(){

//    save values of textbox in variables
    var first_name = $('#first_name').val();
    var last_name = $('#last_name').val();
    var email = $('#email').val();
    var password = $('#password').val();
    var repassword = $('#repassword').val();
    var address = $('#address').val();
    var city = $('#city').val();
    var country = $('#country').val();
    var flag = true;

// validations
    if (first_name == ''){
        $('#error_first_name').addClass('has-error');
        flag = false;
    }else{
            $('#error_first_name').removeClass('has-error').addClass('has-success');
    }

    if (last_name == ''){
        $('#error_last_name').addClass('has-error');
        flag = false;
    }else{
            $('#error_last_name').removeClass('has-error').addClass('has-success');
    }

    if (email == ''){
        $('#error_email').addClass('has-error');
        flag = false;
    }else{
            $('#error_email').removeClass('has-error').addClass('has-success');
    }

    if (password == ''){
        $('#error_password').addClass('has-error');
        flag = false;
    }else{
            $('#error_password').removeClass('has-error').addClass('has-success');
    }

    if (repassword == ''){
        $('#error_repassword').addClass('has-error');
        flag = false;
    }else{
            $('#error_repassword').removeClass('has-error').addClass('has-success');
    }

    if (password != repassword){
        alert ('Password does not match');
        flag = false;
    }

    if (address == ''){
        $('#error_address').addClass('has-error');
        flag = false;
    }else{
        $('#error_address').removeClass('has-error').addClass('has-success');
    }

    if (city == ''){
        $('#error_city').addClass('has-error');
        flag = false;
    }else{
        $('#error_city').removeClass('has-error').addClass('has-success');
    }

    if (country == ''){
        $('#error_country').addClass('has-error');
        flag = false;
    }else{
        $('#error_country').removeClass('has-error').addClass('has-success');
    }

//    if all validations are true then save the data in database
    if (flag == true){
        $.ajax({
            type: 'POST',
            url: '/save-modal-data/',
            data: $('#save_user_data_form').serialize(),
            success: function(){
                bootbox.alert('Data updated Successfully!')
            },
            error: function(){
                alert('error')
            }
        })
    }
});

//when click on add new button modal will open
$('#add_new_user').click(function(){
    $('#save_user_data_form').trigger('reset');
    $('.show_error').removeClass('has-error').addClass('has-success');
    $('#lable_email').show();
    $('#email').show();
    $('#div_password').show();
    $('#div_repassword').show();
    $('#add_user').modal('show');
});

$(document).ready(function() {
    load_user_data();
});
