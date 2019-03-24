// set csrf token
// (function () {
//     var csrftoken = Cookies.get('csrftoken');
//     // console.log(csrftoken);
//     $.ajaxSetup({
//         headers: {"X-CSRFToken": csrftoken}
//     });
// })();
var csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        headers: {"X-CSRFToken": csrftoken}
    });
$(".need_auth").submit(function(e){
         e.preventDefault();
         console.log('inside ajax submit');
         var url = $(this).attr('action');
         // var next_ = $(this).attr('data-next');
         // console.log("data-next is:",next_);
         var data = $(this).serialize();
         $.post(
            url,
            data,
            function(response){
                //almost impossible to see (because of reload)
                //console.log('respones coming');
                //console.log(response);
                // if(next_ !=""){
                //     window.location=next_
                // }else{
                // need to correct var logEr =$("#er").html({{error_message}})
                window.location = response.location
            })
            }
        );
// $("#profile").on('click',function(e){
//     e.preventDefault();
//     url = $(this).attr('href');
//     console.log(url);
//     $.ajax({
//         url:url,
//         type:"GET",
//         success:function(response){
//             console.log("got response");
//             console.log(response.location);
//             window.location = response.location
//         }
//     })


//})

$('#minus').on('click',function(){
        //e.preventDefault();
        var qty = parseInt($("#qty").val());
        if (qty > 0) {
            $('#qty').val(qty - 1);
        }
    qty = $("#qty").val()

});
$('#plus').on('click',function(){
        //e.preventDefault();
        var qty = parseInt($("#qty").val());
        var new_val = $("#qty").val(qty + 1);
    qty = $("#qty").val()

});
