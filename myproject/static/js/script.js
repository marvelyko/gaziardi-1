function addToCart(id){
    storage = window.sessionStorage;
    var cartList = JSON.parse(storage.cart);
    if(cartList.includes(id)){
        cartList = cartList.filter(item => item !== id);
    }
    else{
        cartList.push(id);
    }
    cartCount = document.getElementById('cart-item-count');
    cartCount.innerText = cartList.length;
    storage.setItem('cart',JSON.stringify(cartList));
}

function addToWish(id){
    storage = window.sessionStorage;
    var wishList = JSON.parse(storage.wish);
    if(wishList.includes(id)){
        wishList = wishList.filter(item => item !== id);
    }
    else{
        wishList.push(id);
    }
    wishCount = document.getElementById('wish-item-count');
    wishCount.innerText = wishList.length;
    storage.setItem('wish',JSON.stringify(wishList));
}

window.onload = function(){
    storage = window.sessionStorage;
    if(storage.getItem('wish') == null){
        wishList = new Array();
        storage.setItem('wish',JSON.stringify(wishList));
    }
    if(storage.getItem('cart') == null){
        cartList = new Array();
        storage.setItem('cart',JSON.stringify(cartList));
    }
    var wishList = JSON.parse(storage.wish);
    wishCount = document.getElementById('wish-item-count');
    wishCount.innerText = wishList.length;
    storage.setItem('wish',JSON.stringify(wishList));

    var cartList = JSON.parse(storage.cart);
    cartCount = document.getElementById('cart-item-count');
    cartCount.innerText = cartList.length;
    storage.setItem('cart',JSON.stringify(cartList));
}