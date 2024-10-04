function submitRecommendation(){

    var name = document.getElementById("name");
    var recommendation = document.getElementById("comment");

    //document.getElementById("messageRecomendation").innerHTML = '"' + recommendation + '"' + "<br>"  + name;
    
    if (recommendation.value != null && recommendation.value.trim() != ""){

        console.log("New recommendation added");

        showPopup(true);

        // 1. Create div element
        var element = document.createElement("div");
        
        // 2. setAttribute to div element
        element.setAttribute("class", "recommendation");

        // 3. Add span tag for recomendation value
        element.innerHTML = "\<span class=\"quotes\"\>&#8220;\</span\>" + recommendation.value + "\<span class=\"quotes\"\>&#8221;\</span\>" + " " + name.value ;

        // 4. Add this element at the end of the list of elements
        document.getElementById("all_recommendations").appendChild(element);

        name.value = "";
        recommendation.value = "";
    } 
    
}

function showPopup(bool){
    if (bool){
        document.getElementById("showPopup").style.visibility = 'visible';
    } else {
        document.getElementById("showPopup").style.visibility = 'hidden';
    }
}

