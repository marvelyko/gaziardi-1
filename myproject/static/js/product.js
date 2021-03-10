$(document).ready(function(){
    $(".qtycheckout input").val(quantity);
    $("#price").text(`${(price * quantity).toFixed(2)} ლ`);
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

$('.qty').on("change input", '.quantity', function() {
    // Your code here
    quantity = parseFloat($(".quantity").val()) || quantity;
    if(quantity > available)
        quantity=available;
    else if(quantity < min)
        quantity=min;
    $(".qtycheckout input").val(quantity);
    $("#price").text(`${(price*quantity).toFixed(2)} ლ`);
});

$('#buy').click(()=>{
    var id = parseInt(window.location.href.split("/")[4]);
    window.location.href = `/checkout?id=${id}&qty=${quantity}`
})