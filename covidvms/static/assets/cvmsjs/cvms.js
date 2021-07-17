$(document).ready(function () {
    $("#loginForm").on('submit', function (e) {
        e.preventDefault()
        const url = $(this).attr('action')
        $.ajax({
            url: url,
            type: "POST",
            data: $(this).serializeArray(),
            beforeSend: () => {
                $(".response").html("<span class='spinner-border spinner-border-sm text-info'></span> Authenticating")
                $(".login-btn").attr("disabled", true)
            },
            success: (data) => {
                let response = JSON.parse(data)
                let responseDiv = $(".response");
                if (response.status === "Authenticated") {
                    responseDiv.addClass('alert alert-success fade show w-50')
                    responseDiv.html("<i class='fas fa-check-circle text-success'></i> " + response.status)
                    window.location.href = response.redirect
                } else {
                    responseDiv.addClass('alert alert-danger fade show');
                    responseDiv.html("<i class='fas fa-exclamation-triangle text-warning'></i> " + response.status)
                }
            },
            complete: () => {
                $(".login-btn").attr("disabled", false);
            }
        });
    });
    $("#show-password").on('click', function () {
        $("#hide-password").toggleClass('d-none');
        $(this).toggleClass('d-none');
        $("#password").attr('type', 'text');
    });
    $("#hide-password").on("click", function () {
        $(this).toggleClass('d-none')
        $("#show-password").toggleClass('d-none')
        $("#password").attr('type', 'password');
    });
});