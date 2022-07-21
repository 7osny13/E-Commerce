const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '6fdea477dbmsha0852d88d064a20p151381jsnfc781b9b05cb',
		'X-RapidAPI-Host': 'jumia-service.p.rapidapi.com'
	}
};

fetch('https://jumia-service.p.rapidapi.com/api/product/search/macbook%20pro/50', options)
	.then(response => response.json())
	.then(response => {
                console.log(response)
        response.forEach(function(responses) {
var names = responses.image;
    var idd=responses.id
    var dat=responses.data
var but = document.createElement("img");
    but.value = idd;
    but.src=names;
    but.innerHTML = names;
    but.addEventListener("click",(e)=>{
        document.getElementById("data").innerHTML=''
        x=event.target.value
        //  console.log(users[x-1])
        document.getElementById("img").innerHTML +=responses[x].image
                        
                })
    document.getElementById("1").appendChild(but);
    

})

})