
function display_cart()
{
    let cartItems = localStorage.getItem("productInCart");
    cartItems = JSON.parse(cartItems);
    let product_disp = document.querySelector('.products');

    if(cartItems)
    {
        product_disp.innerHTML ='<tr><th>Nazwa</h><th>cena</th><th>ilosc</th><th>w sumie</th></tr>'
        Object.values(cartItems).map(item=>{

            product_disp.innerHTML += `<tr class="product_row">
            <td>${item.name}</td>
            <td>${item.price} PLN</td>
            <td>${item.in_cart}</td>
            <td>${item.price * item.in_cart} PLN</td>
            </td>
            `
            

        })
        
    }
    
   

   

    
}



display_cart();



