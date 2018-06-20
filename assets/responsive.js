/**
 * Open the menu.
 */
function menuOpen() {
    $("#menu").addClass("mouseover")
    $("#menu-button").addClass("mouseover")
}


/**
 * Close the menu.
 */
function menuClose() {
    $("#menu").removeClass("mouseover")
    $("#menu-button").removeClass("mouseover")
}


/**
 * Toggle the menu.
 */
function menuToggle() {
    if ($("#menu").hasClass("mouseover")) {
        menuClose()
    } else {
        menuOpen()
    }
}


/**
 * Fix the menu for touch devices. Makes the animations instant and brings menu
 * button to the top.
 */
function menuTouch() {
    $("#menu-button").css({
        "z-index": 1,
        "position": "absolute",
        "transition": "background-image .2s"
    })

    $("#menu").css({
        "transition": "width .2s, height .2s, background .2s"
    })
}


$(document).ready(function() {
    if (Modernizr.touch) {
        menuTouch()

        // Toggle menu upon click.
        var menu_last_click = (new Date()).getTime()
        $("#menu").click(function() {
            menu_last_click = (new Date()).getTime()
            menuToggle()
        })

        // Close menu if touched anywhere else.
        $(document).on("click touchend", function() {
            if ((new Date()).getTime() - menu_last_click > 100) {
                menuClose()
            }
        })
    } else {
        // Simply toggle menu via hover.
        $("#menu").mouseout(function() { menuClose() })
        $("#menu").mouseover(function() { menuOpen() })
    }
})

