const openbar = document.querySelector('#toggle-btn');

openbar.addEventListener('click', function(){
    document.querySelector('#sidebar').classList.toggle('expand');
    
})

