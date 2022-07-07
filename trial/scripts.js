const dataObject = [
    {id: "fuel"}, 
    {id: "throttle"}, 
    {id: "speed"},
    {id: "acceleration"},
    {id: "gravity"},
    {id: "distance"},
    {id: "atmosphere"},
    {id: "food"},
    {id: "water"},
    {id: "gc"},
    {id: "mars"},
];

function displayData(){
    for (i=0; i<dataObject.length; i++){
        console.log(i)
        const item = dataObject[i]
        const obj = document.getElementById(item.id+"-inp").value;
        console.log('value for '+i);
        if (obj != "")  {
            console.log('try for '+i);
            document.getElementById(item.id).innerText = obj; 
            console.log('done for '+i);
        }
    }
    const popUp = document.getElementById('popup');
    popUp.style.display = "none";
}

function registerData(){
    const popUp = document.getElementById('popup')
    popUp.style.display = "flex"
}
