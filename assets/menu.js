function menu_over() {
    if (!Modernizr.touch) {
        document.getElementById("menu").className = "mouseover"
    }
}

function menu_out() {
    if (!Modernizr.touch) {
        document.getElementById("menu").className = ""
    }
}

function menu_click() {
    if (Modernizr.touch) {
        menu = document.getElementById("menu")
        if (menu.className == "mouseover") {
            menu.className = ""
        } else {
            menu.className = "mouseover"
        }
    }
}

function menu_fix() {
    if (Modernizr.touch) {
        // Bring the menu button to the top.
        menu_button = document.getElementById("menu_button")
        menu_button.style.zIndex = 1;
        menu_button.style.position = "absolute";

        // Make animation instant
        menu = document.getElementById("menu")
        menu.style.transition = "width .2s, height .2s, background 0s ease .2s";
    }
}