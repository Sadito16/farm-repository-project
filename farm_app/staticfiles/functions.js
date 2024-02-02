function addToCart(item_type, productId) {
    var isAdded = localStorage.getItem("addedToCart_" + item_type + "_" + productId);
    console.log(item_type);
    console.log('-----------------------')
    if (!isAdded) {
        document.getElementById("add-to-cart-" + item_type + "-" + productId).innerText = "Added!";
        localStorage.setItem("addedToCart_"+ item_type + "_" + productId, "true");
    }
    console.log(localStorage);
}

filterSelection("all")

function filterSelection(c) {
    var x, i, welcome_text;
    x = document.getElementsByClassName("filterDiv");
    welcome_text = document.getElementsByClassName("welcome");

    if (c === "all") c = "";
    for (i = 0; i < x.length; i++) {
        w3RemoveClass(x[i], "show");
        if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");

    }
    w3RemoveClass(welcome_text, "show");


}

function w3AddClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) === -1) {
            element.className += " " + arr2[i];
        }
    }
}

function w3RemoveClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}

// Add active class to the current button (highlight it)
var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("navbtn");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("activebtn");
        current[0].className = current[0].className.replace(" activebtn", "");
        this.className += " activebtn";
    });
}




