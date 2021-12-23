
function display_cart()
{
    let cartItems = localStorage.getItem("productInCart");
   
    cartItems = JSON.parse(cartItems);
    let product_disp = document.querySelector('.products');
    let i=1;
    if(cartItems)
    {
        product_disp.innerHTML ='<tr><th>Nazwa</h><th>cena</th><th>ilosc</th><th>w sumie</th></tr>'
        Object.values(cartItems).map(item=>{

            product_disp.innerHTML += `<tr class="product_row">
            <td><button onclick="delete_item(${i})"><ion-icon name="close-circle-outline" ></ion-icon></button>${item.name}</td>
            <td>${item.price} PLN</td>
            <td><ion-icon name="arrow-back-circle-outline"></ion-icon>
            ${item.in_cart}<ion-icon name="arrow-forward-circle-outline"></ion-icon></td>
            <td>${item.price * item.in_cart} PLN</td>
            
            </tr>
            `;
            i++;

        })
       
       disp_total();




        
    }
    

}
function disp_total()
{
    let totalCost = localStorage.getItem("totalCost");
    let cost_disp = document.getElementById('totalCost')
    

    cost_disp.innerHTML = `<div>W sumie: ${totalCost}</div>`;

}

function delete_item(item_id)
{
    var items = JSON.parse( localStorage.getItem("productInCart"));
    var total = localStorage.getItem("totalCost");
    var in_cart = parseInt( localStorage.getItem("cartNumbers"));
    total = total - (items[item_id].price * items[item_id].in_cart);
    in_cart -= parseInt( items[item_id].in_cart);
    delete items[item_id];
    localStorage.setItem("productInCart",JSON.stringify(items));
    localStorage.setItem("totalCost",total);

    localStorage.setItem("cartNumbers",in_cart);

    if(in_cart==0)
    {
        localStorage.removeItem("rest_id")
    }
    display_cart();
    
    
}
function delete_all()
{
    localStorage.clear();
    window.location.reload();
}



display_cart();



