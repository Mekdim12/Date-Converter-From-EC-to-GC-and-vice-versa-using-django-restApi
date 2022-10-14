const form = document.getElementById('form');
 
form.addEventListener('submit', function(e) {
    e.preventDefault()
    
    var fromHolder = document.getElementById("forFrom");
    fromHolder =  fromHolder.options[fromHolder.selectedIndex].value;
    var toHolder = document.getElementById("for-to");
    toHolder = toHolder.options[toHolder.selectedIndex].value;
    var sendingFlag = null;

   
    
    if(fromHolder == toHolder){
        alert("Conversion unit must be altered first ")
        return
    }
   
    if( fromHolder == "EC"){
        sendingFlag = 'E'
    }else if(fromHolder == "GC"){
        sendingFlag = "G"
    }



    var Day = document.getElementById("dayHolder");
    var month = document.getElementById("monthHolder");
    var year = document.getElementById("yearHolder");
    Day = Day.options[Day.selectedIndex].value;
    month = month.options[month.selectedIndex].value;
    year =  year.options[year.selectedIndex].value;



   url =  urlDefiner(Day,month,year,sendingFlag);
   var outPutHolder= document.getElementById('output');

   fetchconversion()
   async function fetchconversion(){

    fetch(url, {
        method: "get",
        headers: {
            "X-Requested-With": 'XMLHttpRequest',
            'Content-Type' : "application/json",
            "Accept": "application/json",
           
        },
        
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        outPutHolder.innerText = "OutPut : "+data[0]+" / "+data[1]+" / "+data[2]
     
        
        console.log("Data is ok", data);
    }).catch(function(ex) {
        console.log("parsing failed", ex);
    });

   }
});




function urlDefiner(day , month , year, conversionFLag){
   
    url = 'http://127.0.0.1:8000/API/Date-retiver/'+day+'-'+month+'-'+year+'/'+conversionFLag;
    return url;
}

textOne = "EC to GC"
textTwo = "GC to EC"
text = ""
let i=0;

counter = 0

function textAnimator(){

    if( counter % 2 == 0){
        text = textOne;
    }else{
         text = textTwo;
    }
    document.getElementById('customeAnimation').innerText = text.slice(0,i)

    i++;
   

    if(i > text.length){
        i=0;
        counter++;
    }
    


}
