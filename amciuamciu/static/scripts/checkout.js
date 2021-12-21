
function display_cart()
{
    let cartItems = localStorage.getItem("productInCart");
    cartItems = JSON.parse(cartItems);
    let product_disp = document.querySelector('.products');

    if(cartItems)
    {
        product_disp.innerHTML =''
        Object.values(cartItems).map(item=>{

            product_disp.innerHTML += `<div class="product col-md-12">
            <p>${item.name}</p>
            <p>${item.price} PLN</p>
            <p>${item.in_cart}</p>
            <p>${item.price * item.in_cart} PLN</p>
            </div>
            `
            

        })
        
    }
    
   

   

    
}



display_cart();



