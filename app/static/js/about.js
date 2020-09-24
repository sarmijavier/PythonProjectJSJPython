
var sebastian = document.querySelector("#sebastian")
var sebastian2 = document.querySelector("#sebastian2")
var imgSeb = document.getElementById('img-seb')

var javier = document.querySelector("#javier")
var javier2 = document.querySelector("#javier2")
var imgJav = document.getElementById('img-jav')

var santiago = document.querySelector("#santiago")
var santiago2 = document.querySelector("#santiago2")
var imgSan = document.getElementById('img-san')

sebastian.addEventListener("mouseover", function () {
    imgSeb.style.display = 'none'
    sebastian2.innerHTML = `<div class="card" style = "width: 18rem;" >
                            <div class="card-body">
                                <h5 class="card-title">Sebastian Benavides</h5>
                                <p class="card-text text-justify">
                                Soy un estudiante de ingeniería de sistemas y computación de la universidad católica de 
                                Colombia, voy en octavo semestre. En mi tiempo libre me gusta jugar fútbol, videojuegos y 
                                escuchar música. Me interesan las aplicaciones de inteligencia artificial, el desarrollo web 
                                y aprender nuevos lenguajes de programación, bases de datos y frameworks de desarrollo.</p>
                            </div>
                        </div >
        `
})

sebastian.addEventListener("mouseout", function () {
    imgSeb.style.display = "block"
    sebastian2.innerHTML = ""
})


javier.addEventListener("mouseover", function () {
    imgJav.style.display = 'none'
    javier2.innerHTML = `<div class="card" style = "width: 18rem;" >
                            <div class="card-body">
                                <h5 class="card-title">Javier Sarmiento</h5>
                                <p class="card-text text-justify">
                                Estudiante de ingeniería de sistemas e informática. Desarrollador e informática en curso. 
                                Me gusta escuchar música y aprender algo nuevo cada día. Nunca pares de aprender y 
                                ¿Cómo puedo ayudarte? 
                                </p>
                            </div>
                        </div >
                        `
})
javier.addEventListener("mouseout", function () {
    imgJav.style.display = "block"
    javier2.innerHTML = ""
})

santiago.addEventListener("mouseover", function () {
    imgSan.style.display = 'none'
    santiago2.innerHTML = `<div class="card" style = "width: 18rem;" >
                            <div class="card-body">
                                <h5 class="card-title">Santiago Restrepo</h5>
                                <p class="card-text text-justify">Soy un estudiante de ingeniería de sistemas en octavo 
                                semestre, tengo 20 años. Me gusta la música, temas relacionados con la ingeniería de datos, 
                                blockchain, aprendizaje automático y desarrollo web.</p>
                            </div>
                        </div >
`
})
santiago.addEventListener("mouseout", function () {
    imgSan.style.display = "block"
    santiago2.innerHTML = ""
})