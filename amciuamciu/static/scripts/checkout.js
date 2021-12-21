
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
            <td><ion-icon name="arrow-back-circle-outline"></ion-icon>
            ${item.in_cart}<ion-icon name="arrow-forward-circle-outline"></ion-icon></td>
            <td>${item.price * item.in_cart} PLN</td>
            <td><ion-icon name="close-circle-outline"></ion-icon><td>
            </tr>
            `
            

        })
       
       disp_total();




        
    }
    

}
function disp_total()
{
    let totalCost = localStorage.getItem("totalCost");
    let cost_disp = document.getElementById('totalCost')
    

    console.log(cost_disp);

    cost_disp.innerHTML = `<div>W sumie: ${totalCost}</div>`;

}



display_cart();



