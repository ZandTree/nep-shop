$('#minus').on('click',function(e){
    e.preventDefault();
    var qty = parseInt($("#qty").val());
    if (qty > 0) {
        $('#qty').val(qty - 1);
    }
    qty = $("#qty").val()

});
$('#plus').on('click',function(e){
    e.preventDefault();
    var qty = parseInt($("#qty").val());
    var new_val = $("#qty").val(qty + 1);
    qty = $("#qty").val()

});
