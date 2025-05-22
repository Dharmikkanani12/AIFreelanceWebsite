// Place your full JS here:
const hamburgerBtn = document.getElementById("hamburger-btn");
const mobileMenu = document.getElementById("mobile-menu");
const mobileMenuCloseBtn = document.getElementById("mobile-menu-close-btn");
const mobileMenuLinks = mobileMenu ? mobileMenu.querySelectorAll("a") : [];
const navLinks = document.querySelectorAll('.nav a');
const sections = document.querySelectorAll('section');

function toggleMobileMenu() {
    if (mobileMenu) {
        mobileMenu.classList.toggle("hidden");
        mobileMenu.classList.toggle("active"); // Add active class
    }
}
if (hamburgerBtn) hamburgerBtn.addEventListener("click", toggleMobileMenu);
if (mobileMenuCloseBtn) mobileMenuCloseBtn.addEventListener("click", toggleMobileMenu);
if (mobileMenuLinks) {
    mobileMenuLinks.forEach(link => {
        link.addEventListener("click", toggleMobileMenu);
    });
}
document.addEventListener('click', (event) => {
    if (mobileMenu && mobileMenu.classList.contains('active') && !mobileMenu.contains(event.target) && event.target !== hamburgerBtn) {
        toggleMobileMenu();
    }
});

function updateActiveNavLink() {
    let currentSectionId = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.scrollY >= sectionTop - 100 && window.scrollY < sectionTop + sectionHeight - 100) {
            currentSectionId = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === currentSectionId) {
            link.classList.add('active');
        }
    });
}
window.addEventListener('scroll', updateActiveNavLink);

function showToast(type, message) {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.classList.add('fade-out');
        setTimeout(() => toast.remove(), 500);
    }, 2000);
}