var quantity = 0.0;
let urlArgs = new URLSearchParams(window.location.search)
var min = parseFloat(urlArgs.get("qty"));
$(document).ready(function(){
    quantity = parseFloat(urlArgs.get("qty"));
    $(".qtycheckout input").val(quantity);
    $("#price").text(`${(price*quantity).toFixed(2)} ლ`);

    $(".qtycheckout input").attr("readonly",true);
});

// Quantity
$('.qtycheckout span').on('click', function () {

    if ($(this).hasClass('btn-plus')) {
        if(quantity < available)
            quantity += min/2;
    } else {
        if (quantity > min) {
            quantity -= min/2;
        }
    }
    $(".qtycheckout input").val(quantity);
    $(".quantity").trigger("change");
});

$('.checkout-summary').on("change input", '.quantity', function() {
    // Your code here
    quantity = parseFloat($(".quantity").val()) || quantity;
    if(quantity > available)
        quantity=available;
    else if(quantity < min)
        quantity=min;
    $(".qtycheckout input").val(quantity);    
    $("#price").text(`${(price*quantity).toFixed(2)} ლ`);
});