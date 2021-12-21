let carts = document.querySelectorAll('.add-to-cart');

let products = document.querySelectorAll('.obj');
let restaurant_ids = document.querySelectorAll('.rest_id');
let menu_ids = document.querySelectorAll('.id');
let dishes_names = document.querySelectorAll('.name');
let prices= document.querySelectorAll('.price');
products_list=[];

console.log(menu_ids[1].innerHTML)
for(var i=0; i<products.length; i++)
{
    
    object={

        id: parseInt( menu_ids[i].innerHTML),
        rest_id: parseInt(restaurant_ids[i].innerHTML),
        name: dishes_names[i].innerHTML,
        price:  parseFloat( prices[i].innerHTML),
        in_cart: 0


    };

    products_list.push(object);



    
}



for(let i=0; i<carts.length; i++)
{
    
    carts[i].addEventListener('click',()=>{

        cartNumber(products_list[i]);
        totalCost(products_list[i]);
        
      
    })
    
}



//zlicz ilość w koszyku
function cartNumber(product)
{
   
    console.log(product);
    let productNo = localStorage.getItem('cartNumbers');
    productNo = parseInt(productNo);
    if(productNo)
    {
        localStorage.setItem('cartNumbers', productNo+1);
        document.querySelector('#cart-no').textContent = productNo+1;
    }
    else{

        localStorage.setItem('cartNumbers',1);
        document.querySelector('#cart-no').textContent = 1;
    }

    setIncart(product);
   
}
function onLoadCartNumbers()
{
    
    let productNo = localStorage.getItem('cartNumbers');
    productNo = parseInt(productNo);
    if(productNo)
    {
       
        document.querySelector('#cart-no').textContent = productNo;
    }
}

function setIncart(product)
{
    let cartItem = localStorage.getItem("productInCart");
    cartItem = JSON.parse(cartItem);
    console.log(product)
    if(cartItem != null)
    {
        if(cartItem[product.id] ==undefined)
        {
            cartItem={
                ...cartItem,
                [product.id]: product
            }
        }
        cartItem[product.id].in_cart +=1;
    }
    else
    {   
        product.in_cart = 1;
        cartItem={
            [product.id]: product
        }

    }
   
    localStorage.setItem("productInCart", JSON.stringify(cartItem));
}

function totalCost(product)
{
    let cartCost = localStorage.getItem('totalCost');
    console.log(product.price);
    

    if(cartCost != null)
    {
        cartCost = parseFloat(cartCost);
        localStorage.setItem("totalCost", cartCost+
        product.price);
    }
    else
    {
        localStorage.setItem("totalCost", product.price);
    }
}

onLoadCartNumbers();