window.addEventListener('load', (event) => {
    console.log('page is fully loaded');

    let form = document.querySelector(".subscribe-form")
    form.addEventListener("submit", function(event){
        console.log(form.email.value);
    });
  });