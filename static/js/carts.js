document.addEventListener("DOMContentLoaded", function () {
    let proSection = document.getElementById('cartdrop')
    async function renderProducts() {
        console.log('here');
        let response = await fetch(`/api/cartitems/`, {
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            method: "GET",
        });
        let data = await response.json()
        console.log('datadan qayidanlar :  ', data);

        let total_price = 0
        let totalItems = 0
        for (let i = 0; i < data.length; i++) {
            if (data[i]['count'] > 0 && data[i]['basket']['status'] == false) {
                totalItems += parseInt(data[i]['count'])
                console.log(totalItems)
                let ids = data[i]['id']
                total_price += parseFloat(data[i]['count'] * data[i]['price'])
                proSection.innerHTML += `
                <div class="sin-itme clearfix">
					<i class="mdi mdi-close"></i>
					<a class="cart-img" href="http://127.0.0.1:8000/en/single_product/${data[i]['productVersion']['id']}/"><img src="${data[i]['productVersion']['images'][0]['image']}"
										alt="" /></a>
					<div class="menu-cart-text">
					
                    <a href="http://127.0.0.1:8000/en/single_product/${data[i]['productVersion']['id']}/">
					<h5>${data[i]['count']} x ${data[i]['productVersion']['title']}</h5>
					</a>
					<span>Color : ${data[i]['productVersion']['color']['title']}</span>
					<span>Size : ${data[i]['productVersion']['size']['title']}</span>
					<strong>$${(data[i]['price'] * data[i]['count']).toFixed(2)}</strong>
					</div>
				</div>
                `

            }
        };
        if (totalItems > 0) {
            document.getElementById('itemnumBer').innerHTML = totalItems;

        }
        let subTotal = document.getElementById('sub_price')
        subTotal.innerHTML = `
        <span> <strong >$ ${total_price.toFixed(2)}</strong></span>

        
        `
    }
    renderProducts();

});
