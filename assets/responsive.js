/**
 * This function should be called when the mouse hovers over the menu.
 */
function menu_over() {
    if (!Modernizr.touch) {
        document.getElementById("menu").className = "mouseover"
    }
}

/**
 * This function should be called when the mouse leaves the menu.
 */
function menu_out() {
    if (!Modernizr.touch) {
        document.getElementById("menu").className = ""
    }
}

/**
 * This function should be called when the user clicks the menu button.
 */
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

/**
 * This function should be called upon loading to fix the menu for touchscreen
 * devices.
 */
function menu_fix() {
    if (Modernizr.touch) {
        // Bring the menu button to the top.
        menu_button = document.getElementById("menu_button")
        menu_button.style.zIndex = 1;
        menu_button.style.position = "absolute";

        // Make animation instant.
        menu = document.getElementById("menu")
        menu.style.transition = "width .2s, height .2s, background 0s ease .2s";
    }
}

$(document).read(menu_fix)