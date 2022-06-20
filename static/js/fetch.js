// -----------------------------------------------------------------------------------
    
//     FETCH JS INDEX
//     ===================
	
//     1. list all blogs in blog page;
//     2. show single-blog blog-detail page;
//     3. list related blogs in blog detail page;
//     4. list latest blogs in home page;
//     5. get data from comment form in blog detail page;
//     6. list comments in blog detail page;
	
// -----------------------------------------------------------------------------------*/

let urlForBlogs = 'http://127.0.0.1:8000/api/blogs/';
let singleBlogID = '';




//     1. list all blogs in blog page;




document.addEventListener("DOMContentLoaded",  function(){
    let blogSection = document.getElementById('blogs')
    async function renderBloglist(){
        let response = await fetch(urlForBlogs, {
            headers: {
                'Content-Type': 'application/json',
                },
            method: "GET",
        });
        let data = await response.json()
        for(let blog of data){
            blogSection.innerHTML += `
            <div class="col-sm-4">
                <div class="l-blog-text">
                    <div class="banner"><a href="#"><img src="${blog.image}" alt="" /></a></div>
                    <div class="s-blog-text">
                        <h4><a href="#">${blog.title}</a></h4>
                        <span>By : ${blog.author} | 123 Like | 45 Comments</span>
                        <p>${blog.content}</p>
                    </div>
                    <div class="date-read clearfix">
                        <a href="#"><i class="mdi mdi-clock"></i> ${blog.created_at}</a>
                        <a href="http://127.0.0.1:8000/api/singleblogpage">read more</a>
                        <p style="display: none;">${blog.id}</p>
                    </div>
                </div>
            </div>
            `;
        }
    }
    renderBloglist();
});




//     2. show single-blog blog-detail page; 
// Burada bir problem var ki, innerHTML += etdiyimiz ucun bloglar comment sectionundan sonra gelir.




document.addEventListener("DOMContentLoaded",  function(){
    let blogSection = document.getElementById('blog-detail')
    async function renderBlogDetail(){
        let response = await fetch(urlForBlogs + singleBlogID, {
            headers: {
                'Content-Type': 'application/json',
                },
            method: "GET",
        });
        let data = await response.json()
        for(let blog of data){
            blogSection.innerHTML += `
        <div class="single-blog-img">
            <img src="${blog.image}" alt="" />
        </div>
        <div class="padding30">
            <div class="blog-text">
                <div class="post-title">
                    <h3>${blog.title}</h3>
                    <ul class="clearfix">
                        <li><i class="pe-7s-user"></i>By :<a href="#">${blog.author}</a><span>|</span></li>
                        <li><i class="pe-7s-comment"></i><a href="#">${blog.created_at}</a><span>|</span></li>
                        <li><i class="pe-7s-like"></i><a href="#">210 Like</a><span>|</span></li>
                        <li><i class="pe-7s-back"></i><a href="#">69 Comments</a></li>
                    </ul>
                </div>
                <p>
                ${blog.content}
                </p>
                <div class="share-tag clearfix">
                    <ul class="blog-share floatleft">
                        <li><h5>share </h5></li>
                        <li><a href="#"><i class="mdi mdi-facebook"></i></a></li>
                        <li><a href="#"><i class="mdi mdi-twitter"></i></a></li>
                        <li><a href="#"><i class="mdi mdi-linkedin"></i></a></li>
                        <li><a href="#"><i class="mdi mdi-vimeo"></i></a></li>
                        <li><a href="#"><i class="mdi mdi-dribbble"></i></a></li>
                        <li><a href="#"><i class="mdi mdi-instagram"></i></a></li>
                    </ul>
                </div>
            </div>
        </div>
            `;
        }
    }
    renderBlogDetail();
});




//     3. list related blogs in blog detail page;




document.addEventListener("DOMContentLoaded",  function(){
    let blogSection = document.getElementById('relatedblogs')
    async function renderRelatedBlogs(){
        let response = await fetch(urlForBlogs, {
            headers: {
                'Content-Type': 'application/json',
                },
            method: "GET",
        });
        let data = await response.json()
        for(let blog of data){
            blogSection.innerHTML += `
            <div class="col-sm-4">
                <div class="l-blog-text">
                    <div class="banner"><a href="#"><img src="${blog.image}" alt="" /></a></div>
                    <div class="s-blog-text">
                        <h4><a href="#">${blog.title}</a></h4>
                        <span>By : ${blog.author} | 123 Like | 45 Comments</span>
                        <p>${blog.content}</p>
                    </div>
                    <div class="date-read clearfix">
                        <a href="#"><i class="mdi mdi-clock"></i> ${blog.created_at}</a>
                        <a href="http://127.0.0.1:8000/api/singleblogpage">read more</a>
                        <p style="display: none;">${blog.id}</p>
                    </div>
                </div>
            </div>
            `;
        }
    }
    renderRelatedBlogs();
});




//     4. list latest blogs in home page;




document.addEventListener("DOMContentLoaded",  function(){
    let blogSection = document.getElementById('latestblog')
    async function renderLatestBlogs(){
        let response = await fetch(urlForBlogs, {
            headers: {
                'Content-Type': 'application/json',
                },
            method: "GET",
        });
        let data = await response.json()
        data = data.reverse()
        for(let blog of data){
            blogSection.innerHTML += `
        <div class="col-sm-4">
            <div class="l-blog-text">
                <div class="banner"><a href="#"><img src="${blog.image}" alt="" /></a></div>
                <div class="s-blog-text">
                    <h4><a href="{% url 'blog-detail' pk=blog.id %}">${blog.title}</a></h4>
                    <span>By : <a href="#">${blog.author}</a> | <a href="#">210 Like</a> | <a href="#">69 Comments</a></span>
                    <p>${blog.content}</p>
                </div>
                <div class="date-read clearfix">
                    <a href="#"><i class="mdi mdi-clock"></i>${blog.created_at}</a>
                    <a href="http://127.0.0.1:8000/api/singleblogpage">read more</a>
                </div>
            </div>
        </div>
            `;
        }
    }
    renderLatestBlogs();
});



//     5. get data from comment form in blog detail page;



(function() {
    let form = document.querySelector('.blogcommentform');
    form.addEventListener('click', async (event) => {
        console.log("sadss")
        event.preventDefault();

        let postData = {
            "comment": form.comment.value 
        }
        let response = await fetch('http://127.0.0.1:8000/api/blogs/3/comments', {
             headers: {
                 'Content-Type': 'application/json',
                 },
             method: "POST",
             body: JSON.stringify(postData)
        });
        let responseData = await response.json();
        alert(responseData) 
    });
 
 })(); 