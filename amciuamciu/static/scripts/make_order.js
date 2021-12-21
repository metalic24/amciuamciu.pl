function order()
{
   
   
   


   
    var orderData ={};
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    orderData['csrfmiddlewaretoken'] = csrf_token;
    orderData['objects'] = localStorage.getItem('productInCart');
    
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
             localStorage.clear();
             
           }
         });

    

}


