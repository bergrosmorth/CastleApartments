// script
function changeprice() {
    var slider = document.getElementById("priceInputID");
    var output = document.getElementById("priceOutputID");
    output.innerHTML = slider.value;
    slider.oninput = function (){
        output.innerHTML = this.value;
    }
}

function changesize() {
    var slider = document.getElementById("sizeInputID");
    var output = document.getElementById("sizeOutputID");
    output.innerHTML = slider.value;
    slider.oninput = function (){
        output.innerHTML = this.value;
    }
}
