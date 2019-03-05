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


$('#minus').on('click',function(e){
        //e.preventDefault();
        var qty = parseInt($("#qty").val());
        if (qty > 0) {
            $('#qty').val(qty - 1);
        }
    qty = $("#qty").val()

});
$('#plus').on('click',function(e){
        //e.preventDefault();
        var qty = parseInt($("#qty").val());
        var new_val = $("#qty").val(qty + 1);
    qty = $("#qty").val()

});
$('#qty_form').on('submit',function(e){
        e.preventDefault();
        //e.preventDefault();// stops browser from sending form and reload
        var url = $(this).attr('action');
        console.log(url);
        //var data = $("#qty").val(); //а представь,у тебя их вагон?
        var data = $(this).serialize();
        $.post(url,data,function(resp){
            $("#note").html('Thanks');
            $("#cart_total").html(resp.qty);
        });
});
