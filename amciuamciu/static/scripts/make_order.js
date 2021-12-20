function order()
{
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    var orderData ={};
    orderData['objects'] = localStorage.getItem('productInCart');
    $.ajax({
        url: '/zamowienia/checkout/',
        type: "POST",
        data: orderData,
       // dataType: "json",
        headers:{
            "X-CSRFToken": csrftoken
        },
        
            
        
        success: function(data){
            console.log("ajax dziala");
         
        }
    });
}

