function order()
{
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    var orderData ={};
    orderData['objects'] =localStorage.getItem('productInCart');
    $.ajax({
        url: '/zamowienia/make_order/',
        type: "POST",
        data: orderData,
       // contentType: "application/json; charset=utf-8",
        //dataType: "json",
        headers:{
            "X-CSRFToken": csrftoken
        },
        
            
        
        success: function(data){
            console.log("ajax dziala");
            console.log(typeof orderData['objects'])
         
        }
    });
}


