function order()
{
   

   
    var orderData ={};
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    orderData['csrfmiddlewaretoken'] = csrf_token;
    orderData['objects'] = localStorage.getItem('productInCart');
    orderData['bill'] = localStorage.getItem('totalCost');
    orderData['rest_id'] = localStorage.getItem('rest_id');

    
    var form = $("#idForm");
   
  //  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    orderData['form']= JSON.stringify( $(form).serializeArray() );
    
    var url = "/zamowienia/make_order/"
    
    $.ajax({
           type: "POST",
           url: url,
           data: orderData, // serializes the form's elements.
           
           success: function(data)
           {
            
            if(data.status == 1){ 
              localStorage.clear();
              window.location = "/zamowienia/pay/"+ data.order_id;
            }
              
             
           }
         });

    

}


