let isClosed = true
const hamburger = document.querySelector(".navbar-toggler")
const navbar = document.querySelector(".navbar-collapse")
const nav = document.querySelector('nav')
const logo = document.querySelector('#logoFriburgo')
hamburger.className = "navbar-toggler text-white"
navbar.style.display = "none"
nav.className = "navbar navbar-expand-lg" 
logo.style.display = 'block'

hamburger.addEventListener('click', ()=>{
    isClosed = !isClosed
    hamburger.className = isClosed ? "navbar-toggler text-white" : "navbar-toggler text-white spin"
    navbar.style.display = isClosed ? "none" : "block"
    nav.className = isClosed ? "navbar navbar-expand-lg" : "navbar navbar-expand-lg showingToo"
    navbar.className = isClosed ? "collapse navbar-collapse" : "collapse navbar-collapse showing"
})