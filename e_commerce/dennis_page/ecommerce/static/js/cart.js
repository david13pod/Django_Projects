var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId', productId, 'action', action)

        console.log('USER', user)
        if (user === 'AnonymousUser'){
            addCookieItem(productId,action)
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function addCookieItem(productId,action){
    console.log('User not authenticated')
    if (action == 'add'){
        if (cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }else{
            cart[productId]['quantity'] += 1
        }
    }
    if (action == 'remove'){
        cart[productId]['quantity'] -= 1
        if (cart[productId]['quantity'] <= 0){
            console.log('Item should be delete')
            delete cart[productId]
        }
    }
    console.log('cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload() //reloading page each time is inefficient for large sites 

}

function updateUserOrder(productId, action){
    console.log('user is logged in, sending data..')

    var url = '/update_item/'

    // fetch api to post data 
    fetch(url, {
        method: 'POST',
        headers : {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        // send as string
        body : JSON.stringify({"productId": productId, "action":action})
    })
    // promise
    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload() //reloading page each time is inefficient for large sites 
    })
}