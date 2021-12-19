var carts = document.querySelectorAll('.add-to-cart');

for(var i=0; i<carts.length; i++)
{
    carts[i].addEventListener('click',()=>{

       cartNumber();
    })
}


function cartNumber()
{
    localStorage.setItem('cartNumbers',1);
}