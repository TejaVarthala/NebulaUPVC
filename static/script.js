document.addEventListener('DOMContentLoaded', function () {
    // Your existing code for menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navList = document.querySelector('nav ul');

    menuToggle.addEventListener('click', function () {
        navList.classList.toggle('show');
    });

    // Initially hide the menu on larger screens
    if (window.innerWidth > 600) {
        navList.classList.remove('show');
    }

});
