$(document).ready(function(){
    var login_type = $('#id_login_type');
    var choice = login_type.val();
    Switch(choice)

    login_type.change(function(){
        var choice = $(this).val();
        Switch(choice);
    });

    function Switch(choice) {
        if (choice == 'key') {
            $('#div_id_password').addClass('hide');
            $('#div_id_private_key').removeClass('hide');
        }else{
            $('#div_id_password').removeClass('hide');
            $('#div_id_private_key').addClass('hide');
        }
    }
});
