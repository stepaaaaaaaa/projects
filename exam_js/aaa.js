const city = document.getElementById("city")
const btn = document.getElementById("find")
const url = "https://api.openweathermap.org/data/2.5/weather?q=dubai&appid=20f0991d489bd96ffe26901a1ac3a0ba"
const req = new XMLHttpRequest();
let gorod = document.getElementById("a1")
let temper = document.getElementById("a2")
let wind = document.getElementById("a3")
let hum = document.getElementById("a4")
let coord = document.getElementById("a5")
let visibility = document.getElementById("a6")
let kartinka = document.getElementById("a7")


function user(event)
{
    event.preventDefault()
    req.open("GET", url.replace("dubai", city.value));
    req.responseType = "json"
    req.onload = () => {
        let data = req.response;
        gorod.innerHTML = `Название города: ${data['name']}`
        let t = temper.innerHTML = `Температура: ${data['main']["temp"]-273} по Цельию`
        console.log(t)
        wind.innerHTML = `Скорость ветра: ${data['wind']["speed"]} метров в секунду`
        hum.innerHTML = `Влажность воздуха: ${data['main']["humidity"]}%`
        coord.innerHTML = `Координаты: Широта ${data['coord']["lat"]}, Долгота ${data['coord']["lon"]}`
        visibility.innerHTML = `Видимость: ${data["visibility"]}`
        
        


    }
    req.send();
}


btn.addEventListener("click", user)