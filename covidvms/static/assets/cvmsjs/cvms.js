$(document).ready(function (){
    $("#loginForm").on('submit', function(e){
        e.preventDefault()
        const url = $(this).attr('action')
        $.ajax({
            url: url,
            type: "POST",
            data: $(this).serializeArray(),
            beforeSend: ()=>{
                $(".response").html("<span class='spinner-border spinner-border-sm text-info'></span> Authenticating")
                    $(".login-btn").attr("disabled", true)
                },
            success: (data)=>{
                let response = JSON.parse(data)
                let responseDiv = $(".response");
                if(response.status === "Authenticated") {
                    responseDiv.addClass('alert alert-success fade show w-50')
                    responseDiv.html("<i class='fas fa-check-circle text-success'></i> "+response.status)
                    window.location.href = response.redirect
                }else{
                    responseDiv.addClass('alert alert-warning fade show');
                    responseDiv.html("<i class='fas fa-exclamation-triangle text-warning'></i> "+response.status)
                }
                },
            complete: ()=>{
                $(".login-btn").attr("disabled", false);
            }
        });
    });
    $("#show-password").on('click', function (){
        $("#hide-password").toggleClass('d-none');
        $(this).toggleClass('d-none');
        $("#password").attr('type', 'text');
    });
    $("#hide-password").on("click", function (){
        $(this).toggleClass('d-none')
        $("#show-password").toggleClass('d-none')
        $("#password").attr('type', 'password');
    });

    $("#feedbackForm").on('submit', function(e){
        e.preventDefault();
        if(!$("#consent").is(':checked'))
        {
            $("#consent-error").html("You must agree with the terms and conditions in order to submit your feed back. Thank You.");
            return false;
        }
        $("#consent-error").html("");
        $.ajax({
            url: $(this).data('url'),
            type: "POST",
            data: $(this).serializeArray(),
            beforeSend: () => {
                $("#submit-btn").attr('disabled', true);
                $("#submit-btn").html("<span class='spinner-border spinner-border-sm'></span> submiting feedback...");
            },
            success: (response) => {
                $("#response").html(response).fadeOut(10000);
            },
            complete: () => {
                $(this).trigger('reset');
                $("#submit-btn").attr('disabled', false);
                $("#submit-btn").html("Submit Your FeedBack");
            }
        });
    });

    $("#feedback-type").on('change', function(){
        if($(this).val() == 'Health Workers Behavior')
        {
            $(".v-center").removeClass('d-none');
            $(".v-name").addClass('d-none');
        }
    });

    $("#next").on('click', ()=> {$(".first-row").toggle(500);$(".second-row").toggle(500);});$("#previous").on('click', ()=> {$(".first-row").toggle(500);$(".second-row").toggle(500);});
    $("#addCitizenForm").on('submit', function(event){
        event.preventDefault();
        let currentObject = $(this);
        $.ajax({
            url: currentObject.attr('action'),
            type: 'POST',
            data: currentObject.serializeArray(),
            beforeSend: () => {
                $("#add-citizen-btn").html("<span class='spinner-border spinner-border-sm'></span> Processing...");
            },
            success: (response) => {
                let interval = 7000;
                $(".response").html(response);
                $(".response").fadeOut(7000);
                setInterval(() => {
                    //window.location.reload();
                }, interval);
            },
            complete: () => {
                $("#add-citizen-btn").html("Add Citizen <i class='fas fa-arrow-circle-up'> </i>");
                //currentObject.trigger('reset');
            }
        })
    });


});

function wordCount(value = 0)
{
    let wordsSpan = document.getElementById('words-left');let min_words = 100;let remaining_word_count = (min_words - value.length);if(value.length > min_words) {wordsSpan.innerHTML = 0;document.getElementById('submit-btn').removeAttribute('disabled');return;}document.getElementById('submit-btn').setAttribute('disabled', true);wordsSpan.innerHTML = remaining_word_count;
}

const registerBtn = document.getElementById('add-citizen-btn');

function ValidateEmail(mail) {
    let emailEl = document.getElementById('email');
    let notification = document.getElementById('email-notif');
    if (/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(mail.toLowerCase())) {
        emailEl.style.borderBottomColor = "green";
        notification.classList.remove("fas", "fa-times-circle", "text-danger");
        notification.classList.add("fas", "fa-check-circle", "text-success");
        registerBtn.removeAttribute('disabled');
    } else {
        emailEl.style.borderBottomColor = "red";
        notification.classList.add("fas", "fa-times-circle", "text-danger");
        registerBtn.setAttribute('disabled', true);
    }
}
function ValidateFname(fname) {
    let nameEl = document.getElementById('surname');
    let notification = document.getElementById('fname-notif');
    if (/^([a-zA-Z]){3,}|([a-zA-Z_]){3,}$/.test(fname)) {
        nameEl.style.borderBottomColor = "green";
        notification.classList.remove("fas", "fa-times-circle", "text-danger");
        notification.classList.add("fas", "fa-check-circle", "text-success");
        registerBtn.removeAttribute('disabled');
    } else {
        nameEl.style.borderBottomColor = "red";
        notification.classList.add("fas", "fa-times-circle", "text-danger");
        registerBtn.setAttribute('disabled', true)
    }
}

        function ValidateLname(lname) {
            let nameEl = document.getElementById('givenname');
            let notification = document.getElementById('lname-notif');
            if (/^([a-zA-Z]){3,}|([a-zA-Z_][a-zA-Z]){3,}$/.test(lname)) {
                nameEl.style.borderBottomColor = "green";
                notification.classList.remove("fas", "fa-times-circle", "text-danger");
                notification.classList.add("fas", "fa-check-circle", "text-success");
                registerBtn.removeAttribute('disabled');
            } else {
                nameEl.style.borderBottomColor = "red";
                notification.classList.add("fas", "fa-times-circle", "text-danger");
                registerBtn.setAttribute('disabled', true)
            }

        }

        function ValidatePhoneNumber(phone) {
            let nameEl = document.getElementById('phone');
            let notification = document.getElementById('phone-notif');
            if (/^([77]|[78]|[75]|[70]|[79]|[3]|[71][4]{1})(\d{8})$/.test(phone)) {
                nameEl.style.borderBottomColor = "green";
                notification.classList.remove("fas", "fa-times-circle", "text-danger");
                notification.classList.add("fas", "fa-check-circle", "text-success");
                registerBtn.removeAttribute('disabled')
            } else {
                nameEl.style.borderBottomColor = "2px solid red";
                notification.classList.add("fas", "fa-times-circle", "text-danger");
                registerBtn.setAttribute('disabled', true)
            }
        }

    function ValidateNIN(nin) {
        let nameEl = document.getElementById('nin');
        let notification = document.getElementById('nin-notif');
        if (/^(([C])([M])([0-9A-Z]){12})$/.test(nin)) {
            nameEl.style.borderBottomColor = "green";
            notification.classList.remove("fas", "fa-times-circle", "text-danger");
            notification.classList.add("fas", "fa-check-circle", "text-success");
            registerBtn.removeAttribute('disabled');
            return (true)
        } else {
            nameEl.style.borderBottomColor = "red";
            notification.classList.add("fas", "fa-times-circle", "text-danger");
            registerBtn.setAttribute('disabled', true)
        }
    }