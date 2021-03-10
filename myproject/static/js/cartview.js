window.onload = function(){
    var totalPrice = 0;
    storage = window.sessionStorage;
    var cartList = storage.cart;
    product_table = document.getElementById("item-list");
    fetch("/cart/",{
        credentials: "same-origin",
        mode: "same-origin",
        method: "post",
        headers: { "Content-Type": "application/json" },
        body: cartList
    }).then(data=>{
        return data.json();
    }).then(data=>{
        products = data.data;
        for(var i=0;i<products.length;i++){
            var tr = product_table.insertRow(-1);
            tr.innerHTML = `
            <td>
                <div class="img">
                    <a href="#"><img src="${products[i].image}" alt="Image"></a>
                    <p>${products[i].name}</p>
                </div>
            </td>
            <td>${products[i].quantity}</td>
            <td>${products[i].price} ₾</td>
            <td>
                <div class="qty">
                    <button class="btn-minus"><i class="fa fa-minus"></i></button>
                    <input type="number" class="quantity" value="1">
                    <button class="btn-plus"><i class="fa fa-plus"></i></button>
                </div>
            </td>
            <td>${products[i].price}₾</td>
            <td><button><i class="fa fa-trash"></i></button></td>
            `;
            totalPrice += products[i].price;
        }
        $(".cart-content").find("span:eq(0)").text(`${totalPrice} ₾`);
    });
}

$('.table-responsive').on("change", '.quantity', function() {
    // Your code here
    var parent = $(this).parents(":eq(2)");
    var qty = parseFloat($(this).val());
    var price = parseFloat(parent.find("td:eq(2)").text().split(" ")[0]);
    var change = (qty*price)-parseFloat(parent.find("td:eq(4)").text());
    parent.find("td:eq(4)").text(`${qty*price} ₾`);
    var totalPrice = $(".cart-content").find("span:eq(0)");
    if(parseFloat(totalPrice.text())){
        totalPrice.text(`${parseFloat(totalPrice.text())+change} ₾`);
    }else{
        totalPrice.text(`${change} ₾`);
    }
    
});

// Quantity
$('.table-responsive').on("click",".qty button",function () {
    var $button = $(this);
    var oldValue = $button.parent().find('input').val();
    var qty = parseFloat($button.parents(":eq(2)").find("td:eq(1)").text());
    if ($button.hasClass('btn-plus')) {
        if(oldValue < qty)
            var newVal = parseFloat(oldValue) + 1;
        else
            var newVal = oldValue;
    } else {
        if (oldValue > 0) {
            var newVal = parseFloat(oldValue) - 1;
        } else {
            newVal = 0;
        }
    }
    $button.parent().find('input').val(newVal);
    $(".quantity").trigger("change");
});