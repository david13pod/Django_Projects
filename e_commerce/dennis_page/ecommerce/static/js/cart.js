var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId', productId, 'action', action)

        console.log('USER', user)
        if (user === 'AnonymousUser'){
            console.log('not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
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