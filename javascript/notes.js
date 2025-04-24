let images = ["https://www.mountain-forecast.com/system/images/24500/large/Mount-Timpanogos.jpg?1532401039", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ1hTOCpIAgnA4wOl3DtnYe91LwykHPRYKhQ&s", "https://i.etsystatic.com/37394532/r/il/27e6c7/5018857984/il_fullxfull.5018857984_l9h3.jpg", "https://cdn.kslnewsradio.com/kslnewsradio/wp-content/uploads/2019/06/GettyImages-512336000.jpg"]
let counter = 0

function change(){
    if (counter < images.length){
       document.getElementById("img").src = images[counter] 
       counter += 1
    }else{
        counter = 0
        document.getElementById("img").src = images[counter]
    }
    
}

function hello(){
    let name = window.prompt("What is your name?", "Koro Sensei")
    document.getElementById("title").innerHTML = "Hello " + name + "!"
}
function hover(){
    document.getElementById("img").src = "https://www.mountain-forecast.com/system/images/24500/large/Mount-Timpanogos.jpg?1532401039"
}
function leave(){
    document.getElementById("img").src = "https://i.etsystatic.com/37394532/r/il/27e6c7/5018857984/il_fullxfull.5018857984_l9h3.jpg"
}

function pop(){
    window.alert("Really don't click that!")
}
function show(){
    document.getElementById("lost").style.display = "block"
}

function view(){
    if(document.getElementById("more").style.display == "block"){
        document.getElementById("more").style.display = "none"
        document.getElementById("shw").innerHTML = "Show More"
    }else{
        document.getElementById("more").style.display = "block"
        document.getElementById("shw").innerHTML = "Show Less"
    }
    
}