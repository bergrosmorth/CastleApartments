function changeprice() {
    var slider = document.getElementById("priceInputID");
    var output = document.getElementById("priceOutputID");
    output.innerHTML = slider.value;
    slider.oninput = function (){
        output.innerHTML = this.value;
    };
}

function changesize() {
    var slider = document.getElementById("sizeInputID");
    var output = document.getElementById("sizeOutputID");
    output.innerHTML = slider.value;
    slider.oninput = function (){
        output.innerHTML = this.value;
    };
}

$(document).ready(function () {
    $('#searchbtn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#searchbox').val();
        $.ajax({
            url: '/apartment/?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                var newHTML = resp.data.map(d => {
                    let id = $(d.id);
                    return ` <div class="apartment">
                            <a href="/apartment/$(d.id)">
                                <img class="apartment-img" src="apartment.apartmentimage_set.first.image}}"/>
                                <h4> ${d.address}</h4>
                                <p> ${d.price}kr.</p>
                            </a>
                        </div>`
                });
                console.log(newHTML);
                $('#apartments').html(newHTML.join(''));
                $('#searchbox').val('')
            },
            error: function (xhr, status, error) {
                console.error(error)
            }
        });
    });
});








