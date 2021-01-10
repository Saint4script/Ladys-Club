function sendForm(){
    let fd = new FormData(registration_form);

    $.ajax({
        type: "POST",
        url: '/send_form/',
        data: fd,
        contentType: false,
        processData: false
    }).done(function (result) {
        if (result["status"] == "Ok"){
            alert("Создали");      
        }else{
            alert("что-то пошло не так");
        }
    })
    .fail(function (jqXHR, exception) {
        // Our error logic here
        var msg = '';
        if (jqXHR.status === 0) {
            msg = 'Not connect.\n Verify Network.';
        } else if (jqXHR.status == 404) {
            msg = 'Requested page not found. [404]';
        } else if (jqXHR.status == 500) {
            msg = 'Internal Server Error [500].';
        } else if (exception === 'parsererror') {
            msg = 'Requested JSON parse failed.';
        } else if (exception === 'timeout') {
            msg = 'Time out error.';
        } else if (exception === 'abort') {
            msg = 'Ajax request aborted.';
        } else {
            msg = 'Uncaught Error.\n' + jqXHR.responseText;
        }
        console.log(msg);
    });
}


$(document).ready(function() {  
    let form  = document.getElementById("registration_form");
    var csrftoken = form.elements.csrfmiddlewaretoken.value;

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    
});
