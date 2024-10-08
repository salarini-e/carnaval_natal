window.onload = function(){
    const vara = new Vara(
        "#natal-titulo", 
        "https://raw.githubusercontent.com/akzhy/Vara/master/fonts/Satisfy/SatisfySL.json",
        [
            {
                text: "Casa do Papai Noel",
                y: 250,
                fromCurrentPosition: {y:false},
                duration:3000
            },
        ],
        {
            strokeWidth: 2,
            color: "#fff",
            fontSize:60,
            textAlign:"center"
        }

)
vara.ready(function(){
    var erase = false;
    vara.animationEnd(function(i, o){
        if(i == "no_erase") erase = false;
        if(erase){
            o.container.style.transition = "opacity 1s 1s";
            o.container.style.opacity = 0;
        }
    })
});
}