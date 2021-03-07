function sendForm() {
    let fd = new FormData(registration_form);
    // let loadGif = $.getElementByClass("gif-container")[0];
    $('.gif-container').css('display', 'block');
    $('.gif-shadow').css('display', 'block');
    $('.fieldset')[0].disabled = true;
    $.ajax({
            type: "POST",
            url: '/send_form/',
            data: fd,
            contentType: false,
            processData: false
        }).done(function(result) {
            $('.gif-container').css('display', 'none');
            $('.gif-shadow').css('display', 'none');
            $('.fieldset')[0].disabled = false;
            if (result["status"] == "OK") {
                alert("Создали");
            } else {
                alert("что-то пошло не так");
            }
        })
        .fail(function(jqXHR, exception) {
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

function setSizeForNewsImages() {
    let imgDiv = $(".image")[0];
    let newsImages = $(".image>img");
    newsImages.each(function() {
        $(this).css("width", imgDiv.offsetWidth);
        $(this).css("height", imgDiv.offsetHeight);

    })
}


$(document).ready(function() {
    // code for form sending
    let form = document.getElementById("registration_form");
    var csrftoken = form.elements.csrfmiddlewaretoken.value;

    if ($(".gallery-cell").length == 0) {
        $(".news-wrapper").css("display", "none")
    }

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

    setSizeForNewsImages();

});

$(window).resize(() => {
    setSizeForNewsImages();
})