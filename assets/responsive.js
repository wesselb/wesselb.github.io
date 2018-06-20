/**
 * This function should be called when the mouse hovers over the menu.
 */
function menuOver() {
    if (!Modernizr.touch) {
        $("#menu").addClass("mouseover")
    }
}

/**
 * This function should be called when the mouse leaves the menu.
 */
function menuOut() {
    if (!Modernizr.touch) {
        $("#menu").removeClass("mouseover")
    }
}

var last_menu_click = (new Date()).getTime()  // Timestamp of last click

/**
 * This function should be called when the user clicks the menu button.
 */
function menuClick() {
    if (Modernizr.touch) {
        // Record click time.
        last_menu_click = (new Date()).getTime()

        // Toggle menu.
        if ($("#menu").hasClass("mouseover")) {
            $("#menu").removeClass("mouseover")
        } else {
            $("#menu").addClass("mouseover")
        }
    }
}

/**
 * This function should be called whenever the user clicks anywhere. Since the
 * body is a parent of the menu, this event should always come second.
 */
function menuDocumentClick() {
    if (Modernizr.touch) {
        // Close menu if clicked anywhere else.
        ms_since_last_menu_click = (new Date()).getTime() - last_menu_click
        if (ms_since_last_menu_click > 100) {
            $("#menu").removeClass("mouseover")
        }
    }
}

/**
 * This function should be called upon loading to fix the menu for touchscreen
 * devices.
 */
function menuFix() {
    if (Modernizr.touch) {
        // Bring the menu button to the top.
        menu_button = document.getElementById("menu-button")
        menu_button.style.zIndex = 1
        menu_button.style.position = "absolute"

        // Make animation instant.
        menu = document.getElementById("menu")
        menu.style.transition = "width .2s, height .2s, background 0s ease .2s";
    }
}


$(document).ready(function() {
    // Load events.
    $("#menu").mouseout(menuOut)
    $("#menu").mouseover(menuOver)
    $("#menu").click(menuClick)
    $(document).click(menuDocumentClick)
    //   Make it also work on touch devices.
    $(document).on("click touchend", menuDocumentClick)

    // Fix menu.
    menuFix()
})

