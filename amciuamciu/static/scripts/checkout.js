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
        product_disp.innerHTML =`<div class="products_div">`;
        Object.values(cartItems).map(item=>{

            product_disp.innerHTML += `<div class="product">
            <p>${item.name}</p>
            <p>${item.price} PLN</p>
            <p>${item.in_cart}</p>
            <p>${item.price * item.in_cart} PLN</p>
            </div>
            `
            

        })
        product_disp.innerHTML+=`<div>`;
    }
    
   

   

    
}



display_cart();

onLoadCartNumbers();

