var carts = document.querySelectorAll('.add-to-cart');

for(var i=0; i<carts.length; i++)
{
    carts[i].addEventListener('click',()=>{

       cartNumber();
    })
}

//zlicz ilość w koszyku
function cartNumber()
{
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