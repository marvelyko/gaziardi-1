$(".status button").click(()=>{
    let id = $("#order-id").val()
    window.location.href=`/checkout/status/${id}`
})