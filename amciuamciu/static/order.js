let carts = document.querySelectorAll('.add-to-cart');

let products = document.querySelectorAll('.obj');
let restaurant_ids = document.querySelectorAll('.rest_id');
let menu_ids = document.querySelectorAll('.id');
let dishes_names = document.querySelectorAll('.name');
let prices= document.querySelectorAll('.price');
products_list=[];


for(var i=0; i<products.length; i++)
{
    
    object={

        id: parseInt( menu_ids[i].innerHTML),
        rest_id: parseInt(restaurant_ids[i].innerHTML),
        name: dishes_names[i].innerHTML,
        price: parseInt( prices[i].innerHTML),
        in_cart: 0


    };

    products_list.push(object);



    
}



for(let i=0; i<carts.length; i++)
{
    
    carts[i].addEventListener('click',()=>{

        cartNumber(products_list[i]);
       
        
      
    })
    
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

   
}

onLoadCartNumbers();