const BasketLogic = {
	productManager(productId, quantity, template) {
		fetch('http://127.0.0.1:8000/api/cart/', {
			method: 'POST',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json',
                'Accept': 'application/json',
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			},
			body: JSON.stringify({
				'product': productId,
				'quantity': quantity,
				'template': template,
			})
		})
			.then(response => response.json())
			.then(data => {
                console.log(data)
				if (data.success) {
					cartManager()
					// cartItemManager()
				} else {
					alert(data.message);
				}
			});
			console.log(productId)
	}
}


const addToBasket = document.querySelectorAll('.add_to_cart');
addToBasket.forEach(item => {
	item.onclick = function () {
		if (item.classList.contains('disabled') == false) {
			if (item.tagName == 'A') {
				item.style.backgroundColor = "green";
				item.style.color = "white";
				item.innerText = "Added to cart"
				item.classList.add('disabled')
				setTimeout(() => {
					item.style.background = "";
					item.style.color = "";
					item.innerText = "Add to cart"
					item.classList.remove('disabled')
				}, 1000);
			} else {
				item.parentElement.style.backgroundColor = "green";
				item.style.color = "white";
				item.classList.add('disabled')
				setTimeout(() => {
					item.parentElement.style.background = "";
					item.style.color = "";
					item.classList.remove('disabled')
				}, 1000);
			}
			const productId = this.getAttribute('data');
			template = "product-list.html"
			try {
				quantity = document.getElementById('quantity').value;
			} catch {
				quantity = 1
			}
			BasketLogic.productManager(productId, quantity, template);
			

		}
	}
})

mdi_close = document.getElementsByClassName('mdi-close')
product_count = document.getElementById("product_count")
basketItem = document.getElementById("cartdrop")
total = document.getElementById("total")

function cartManager() {
	fetch('http://127.0.0.1:8000/api/cart-item/', {
		method: 'GET',
		credentials: 'include',
		headers: {
			'Content-Type': 'application/json',
			'Authorization': `Bearer ${localStorage.getItem('token')}`
		}
	})
		.then(response => response.json())
		.then(data => {
			html = ''
			total_price = 0
			let count = 0
            console.log(data)
			if (data.length > 0 && data[0]['cart']['is_ordered'] == false) {
				for (let i = 0; i < data.length; i++) {
					total_price += parseFloat(data[i]['quantity'] * data[i]['productVersion']['new_price'])
					if (data[i]['quantity'] > 0) {
						count += 1
						html += `
					<div class="sin-itme clearfix">
					<a data="${data[i]['productVersion']['id']}" class="remove_from_cart" onmouseover="removeFromCart()"> <i class="mdi mdi-close"></i> </a>
					<a class="cart-img" href="http://127.0.0.1:8000/en/single_product/${data[i]['productVersion']['id']}/"><img src='${data[i]['productVersion']['images'][0]['image']}'
					alt="" /></a>
					<div class="menu-cart-text">
					<a href="http://127.0.0.1:8000/en/single_product/${data[i]['productVersion']['id']}/">
					<h5>${data[i]['quantity']} x ${data[i]['productVersion']['title']}</h5>
					</a>
					<span>Color : ${data[i]['productVersion']['colors']['title']}</span>
					<span>Size : ${data[i]['productVersion']['sizes']['title']}</span>
					<strong>$${parseFloat(data[i]['quantity'] * data[i]['productVersion']['new_price']).toFixed(2)}</strong>
					</div>
					</div>
					`
					}
				}
			}
			basketItem.innerHTML = html
			basketItem.innerHTML += `<div class="total">
			<span>total <strong>= $${total_price.toFixed(2)}</strong></span>
			</div>
			`
			total.innerText = `$${total_price.toFixed(2)}`
			product_count.innerText = count
			try {
				cartItemManager()
			} catch {
			}
			try {
				checkoutManager()
			} catch {
			}
		});
}

window.addEventListener('DOMContentLoaded', (event) => {
	cartManager()
    
});

function removeFromCart() {
	var remove_from_cart = document.getElementsByClassName("remove_from_cart")
    
	for (let i = 0; i < remove_from_cart.length; i++) {
		remove_from_cart[i].onclick = function () {
			productId = this.getAttribute('data')
			quantity = 1
			template = "remove_from_cart"
			BasketLogic.productManager(productId, quantity, template);
            
		}
	}
}


// wishlistUrl = location.origin + '/en/api/wishlist/'
// const WishlistLogic = {
// 	wishlistPostManager(productId) {
// 		fetch(wishlistUrl, {
// 			method: 'POST',
// 			credentials: 'include',
// 			headers: {
// 				'Content-Type': 'application/json',
// 				'Authorization': `Bearer ${localStorage.getItem('token')}`
// 			},
// 			body: JSON.stringify({
// 				'product': productId,
// 			})
// 		})
// 			.then(response => response.json())
// 			.then(data => {
// 				try {
// 					wishlistManager()
// 				}catch{
// 				}
// 			});
// 	}
// }



// var add_to_wishlist = document.getElementsByClassName('add_to_wishlist');
// for (let i = 0; i < add_to_wishlist.length; i++) {
// 	add_to_wishlist[i].onclick = function () {
// 		const productId = this.getAttribute('data');
// 		WishlistLogic.wishlistPostManager(productId);
// 	}
// }


