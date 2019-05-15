function changeprice() {
    var slider = document.getElementById("priceInputID");
    var output = document.getElementById("priceOutputID");
    output.innerHTML = slider.value;
    slider.onchange = function () {
        output.innerHTML = this.value;
        let millions = this.value * 1000000
        jQuery.ajax({
            url: '/apartment/?price_filter=' + millions,
            type: 'GET',
            success: function (resp) {

                var newHTML = resp.data.map(d => {
                    console.log(d.id)
                    d.price = d.price.toLocaleString()
                    return ` <div class="apartment">
                            <a href="/apartment/${d.id}">
                                <img class="apartment-img" src=${d.firstimage}>
                                <h4> ${d.address}</h4>
                                <p> ${d.price} kr.</p>
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
    };
}

function changesize() {
    var slider = document.getElementById("sizeInputID");
    var output = document.getElementById("sizeOutputID");
    output.innerHTML = slider.value;
    slider.onchange = function () {
        output.innerHTML = this.value;
        jQuery.ajax({
            url: '/apartment/?size_filter=' + this.value,
            type: 'GET',
            success: function (resp) {
                var newHTML = resp.data.map(d => {
                    d.price = d.price.toLocaleString()
                    return ` <div class="apartment">
                            <a href="/apartment/${d.id}">
                                <img class="apartment-img" src=${d.firstimage}>
                                <h4> ${d.address}</h4>
                                <p> ${d.price} kr.</p>
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
    };
}

jQuery(document).ready(function () {
    $('#rooms').on('change', function(e) {
        e.preventDefault();
        var room = $('#rooms').val();
        jQuery.ajax({
            url: '/apartment/?room_filter=' + room,
            type: 'GET',
            success: function (resp) {
                var newHTML = resp.data.map(d => {
                    d.price = d.price.toLocaleString()
                    return ` <div class="apartment">
                            <a href="/apartment/${d.id}">
                                <img class="apartment-img" src=${d.firstimage}>
                                <h4> ${d.address}</h4>
                                <p> ${d.price} kr.</p>
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

jQuery(document).ready(function () {
    $('#zip').on('change', function(e) {
        e.preventDefault();
        let zip = $('#zip').val();
        let zipint = parseInt(zip)
        jQuery.ajax({
            url: '/apartment/?zip_filter=' + zipint,
            type: 'GET',
            success: function (resp) {
                var newHTML = resp.data.map(d => {
                    let sid = $(d.id);
                    d.price = d.price.toLocaleString()
                    return ` <div class="apartment">
                            <a href="/apartment/${d.id}">
                                <img class="apartment-img" src=${d.firstimage}>
                                <h4> ${d.address}</h4>
                                <p> ${d.price} kr.</p>
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



jQuery(document).ready(function () {
    $('#searchbtn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#searchbox').val();
        $.ajax({
            url: '/apartment/?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                var newHTML = resp.data.map(d => {
                    d.price = d.price.toLocaleString()
                    return ` <div class="apartment">
                    <a href="/apartment/${d.id}">
                        <img class="apartment-img" src="${d.firstimage}">
                        <h4> ${d.address}</h4>
                        <p> ${d.price} kr.</p>
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


var postnr = ["101 Reykjavík", "103 Reykjavík", "104 Reykjavík", "105 Reykjavík", "107 Reykjavík", "108 Reykjavík", "109 Reykjavík", "110 Reykjavík", "111 Reykjavík", "112 Reykjavík", "113 Reykjavík", "116 Reykjavík", "121 Reykjavík", "123 Reykjavík", "124 Reykjavík",
    "125 Reykjavík", "127 Reykjavík", "128 Reykjavík", "129 Reykjavík", "130 Reykjavík", "132 Reykjavík", "162 Reykjavík", "170 Seltjarnarnesi", "172 Seltjarnarnesi", "190 Vogum", "191 Vogum", "200 Kópavogi", "201 Kópavogi", "202 Kópavogi", "203 Kópavogi", "210 Garðabæ",
    "212 Garðabæ", "220 Hafnarfirði", "221 Hafnarfirði", "222 Hafnarfirði", "225 Garðabæ", "230 Reykjanesbæ", "232 Reykjanesbæ", "233 Reykjanesbæ", "235 Keflavíkurflugvöllur", "240 Grindavík", "241 Grindavík", "245 Sandgerð", "246 Sandgerði", "250 Garði", "251 Garði",
    "260 Reykjanesbæ", "262 Reykjanesbæ", "270 Mosfellsbæ", "271 Mosfellsbæ", "276 Mosfellsbæ", "300 Akranesi", "301 Akranesi", "302 Akranesi", "310 Borgarnesi", "311 Borgarnesi", "320 Reykholt í Borgarfirði", "340 Stykkishólmi", "341 Stykkishólmi", "345 Flatey á Breiðafirði",
    "350 Grundarfirði", "351 Grundarfirði", "355 Ólafsvík", "356 Snæfellsbæ", "360 Hellissandi", "370 Búðardal", "371 Búðardal", "380 Reykhólahreppi", "381 Reykhólahreppi", "400 Ísafirði", "401 Ísafirði", "410 Hnífsdal", "415 Bolungarvík", "416 Bolungarvík", "420 Súðavík",
    "421 Súðavík", "425 Flateyri", "426 Flateyri", "430 Suðureyri", "431 Suðureyri", "450 Patreksfirði", "451 Patreksfirði", "460 Tálknafirði", "461 Tálknafirði", "465 Bíldudal", "466 Bíldudal", "470 Þingeyri", "471 Þingeyri", "500 Stað", "510 Hólmavík", "511 Hólmavík",
    "512 Hólmavík", "520 Drangsnesi", "524 Árneshreppi", "530 Hvammstanga￿", "531 Hvammstanga", "540 Blönduósi", "541 Blönduósi", "545 Skagaströnd", "546 Skagaströnd", "550 Sauðárkróki", "551 Sauðárkróki", "560 Varmahlíð", "561 Varmahlíð", "565 Hofsós", "566 Hofsós",
    "570 Fljótum", "580 Siglufirði", "581 Siglufirði", "600 Akureyri", "601 Akureyri", "602 Akureyri", "603 Akureyri", "610 Grenivík", "611 Grímsey", "616 Grenivík", "620 Dalvík", "621 Dalvík", "625 Ólafsfirði", "626 Ólafsfirði", "630 Hrísey", "640 Húsavík", "641 Húsavík",
    "645 Fosshólli", "650 Laugum", "660 Mývatni", "670 Kópaskeri", "671 Kópaskeri", "675 Raufarhöfn", "676 Raufarhöfn", "680 Þórshöfn", "681 Þórshöfn", "685 Bakkafirði", "686 Bakkafirði", "690 Vopnafirði", "691 Vopnafirði", "700 Egilsstöðum", "701 Egilsstöðum", "710 Seyðisfirði",
    "711 Seyðisfirði", "715 Mjóafirði", "720 Borgarfirði", "721 Borgarfirði", "730 Reyðarfirði", "731 Reyðarfirði", "735 Eskifirði", "736 Eskifirði", "740 Neskaupsstað", "741 Neskaupsstað", "750 Fáskrúðsfirði", "751 Fáskrúðsfirði", "755 Stöðvarfirði", "756 Stöðvarfirði", "760 Breiðdalsvík",
    "761 Breiðdalsvík", "765 Djúpavogi", "766 Djúpavogi", "780 Höfn í Hornafirði", "781 Höfn í Hornafirði", "785 Öræfum", "800 Selfossi", "801 Selfossi", "802 Selfossi", "810 Hveragerði", "815 Þorlákshöfn", "816 Ölfus", "820 Eyrarbakka", "825 Stokkseyri", "840 Laugarvatni", "845 Flúðum",
    "846 Flúðum", "850 Hellu", "851 Hellu", "860 Hvolsvelli", "861 Hvolsvelli", "870 Vík", "871 Vík", "880 Kirkjubæjarklaustri", "881 Kirkjubæjarklaustri", "900 Vestmannaeyjum", "902 Vestmannaeyjum"];
$('zip').empty();
$.each(postnr, function (i, p) {
    $('#zip').append($('<option></option>').val(p).html(p));
    });