function onLoadCartNumbers()
{
    
    let productNo = localStorage.getItem('cartNumbers');
    productNo = parseInt(productNo);
    if(productNo)
    {
       
        document.querySelector('#cart-no').textContent = productNo;
    }
}
function display_cart()
{
    let cartItems = localStorage.getItem("productInCart");
    cartItems = JSON.parse(cartItems);
    let product_disp = document.querySelector('.products');

    if(cartItems)
    {
        product_disp.innerHTML = '';
        Object.values(cartItems).map(item=>{

            product_disp.innerHTML+= '<div class="product"'+item.price+'/div>';

        })
    }
    
   

   

    
}

display_cart();

onLoadCartNumbers();

