function toggleMenu(){
    const menu = document.querySelector('.menu');
    const open = document.querySelector(".menu_mobile")
    const close = document.querySelector(".menu_mobile--close")

    if (menu.style.display == "none") {
        menu.style.display = "block";
        open.style.display = "none";
        close.style.display = "block";
    } else {
        menu.style.display = "none";
        open.style.display = "block";
        close.style.display = "none";
    }

}

