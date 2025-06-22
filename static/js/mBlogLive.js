document.addEventListener('DOMContentLoaded', () => {
    console.log("Webpack is working with Django! - dj static js");

    // ========================== Navbar js =====================================
    // ==========================================================================
    // --- Mobile Menu Toggle ---
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('#mobile-menu');
    const menuIconOpen = mobileMenuButton.querySelector('.menu-icon-open'); // Hamburger icon
    const menuIconClose = mobileMenuButton.querySelector('.menu-icon-close'); // X icon

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', () => {
            const isMenuOpen = mobileMenu.classList.contains('open');

            if (isMenuOpen) {
                // Close menu
                mobileMenu.classList.remove('open');
                mobileMenu.setAttribute('aria-expanded', 'false');
                menuIconOpen.classList.remove('hidden');
                menuIconClose.classList.add('hidden');
            } else {
                // Open menu
                mobileMenu.classList.add('open');
                mobileMenu.setAttribute('aria-expanded', 'true');
                menuIconOpen.classList.add('hidden');
                menuIconClose.classList.remove('hidden');
            }
        });
    }

    // --- Dropdown Functionality (Desktop and Mobile) ---
    // Use event delegation for all dropdown buttons
    document.body.addEventListener('click', (event) => {
        const target = event.target;
        const dropdownButton = target.closest('.nav-dropdown-btn') || target.closest('.mobile-dropdown-btn');

        // Close all other open dropdowns first
        document.querySelectorAll('.dropdown-menu').forEach(menu => {
            if (menu.id !== (dropdownButton ? dropdownButton.dataset.dropdown : null) && !menu.classList.contains('hidden')) {
                menu.classList.add('hidden');
                // Also reset icon if it's a dropdown button with an SVG
                const parentButton = menu.previousElementSibling;
                if (parentButton && parentButton.tagName === 'BUTTON' && parentButton.querySelector('svg')) {
                    parentButton.querySelector('svg').classList.remove('rotate-180');
                }
            }
        });

        if (dropdownButton) {
            const dropdownId = dropdownButton.dataset.dropdown;
            const dropdownMenu = document.getElementById(dropdownId);
            const dropdownIcon = dropdownButton.querySelector('svg');

            if (dropdownMenu) {
                // Toggle the hidden class
                dropdownMenu.classList.toggle('hidden');
                // Toggle the icon rotation
                if (dropdownIcon) {
                    dropdownIcon.classList.toggle('rotate-180');
                }
                // Prevent event from bubbling up to close-on-outside-click listener
                event.stopPropagation();
            }
        }
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', (event) => {
        // Check if the click was outside any dropdown button or menu
        if (!event.target.closest('.dropdown-menu') && !event.target.closest('.nav-dropdown-btn') && !event.target.closest('.mobile-dropdown-btn')) {
            document.querySelectorAll('.dropdown-menu').forEach(menu => {
                menu.classList.add('hidden');
                const parentButton = menu.previousElementSibling;
                if (parentButton && parentButton.tagName === 'BUTTON' && parentButton.querySelector('svg')) {
                    parentButton.querySelector('svg').classList.remove('rotate-180');
                }
            });
        }
    });


    // --- Dark Mode Toggle ---
    const darkModeToggle = document.getElementById('darkModeToggle');
    const htmlElement = document.documentElement; // The <html> tag
    const sunIcon = darkModeToggle.querySelector('.sun-icon');
    const moonIcon = darkModeToggle.querySelector('.moon-icon');

    // Function to update icon visibility
    function updateDarkModeIcons(isDarkMode) {
        if (isDarkMode) {
            sunIcon.classList.add('hidden');
            moonIcon.classList.remove('hidden');
        } else {
            sunIcon.classList.remove('hidden');
            moonIcon.classList.add('hidden');
        }
    }

    // Initialize theme based on localStorage or system preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlElement.classList.remove('dark', 'light'); // Remove existing classes first
        htmlElement.classList.add(savedTheme);
        updateDarkModeIcons(savedTheme === 'dark');
    } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        // If no preference saved, check system preference
        htmlElement.classList.add('dark');
        localStorage.setItem('theme', 'dark'); // Save system preference as default
        updateDarkModeIcons(true);
    } else {
        htmlElement.classList.add('light'); // Default to light if no preference
        localStorage.setItem('theme', 'light'); // Save light as default
        updateDarkModeIcons(false);
    }

    // Add event listener for the toggle button
    darkModeToggle.addEventListener('click', () => {
        if (htmlElement.classList.contains('dark')) {
            htmlElement.classList.remove('dark');
            htmlElement.classList.add('light');
            localStorage.setItem('theme', 'light');
            updateDarkModeIcons(false);
        } else {
            htmlElement.classList.remove('light');
            htmlElement.classList.add('dark');
            localStorage.setItem('theme', 'dark');
            updateDarkModeIcons(true);
        }
    });

    // ========================== carousal js =====================================
    // ============================================================================
    // Simple carousel functionality
    const slides = document.querySelector('.flex.transition-transform');
    const slideCount = document.querySelectorAll('.min-w-full').length;
    let currentIndex = 0;

    function goToSlide(index) {
        console.log(index)
        currentIndex = index;
        slides.style.transform = `translateX(-${currentIndex * 100}%)`;

        // Update indicators
        document.querySelectorAll('.absolute.bottom-4 button').forEach((btn, i) => {
            btn.classList.toggle('bg-white/80', i === currentIndex);
            btn.classList.toggle('bg-white/50', i !== currentIndex);
        });
    }

    // Next slide
    document.querySelector('.absolute.right-4').addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % slideCount;
        goToSlide(currentIndex);
    });

    // Previous slide
    document.querySelector('.absolute.left-4').addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + slideCount) % slideCount;
        goToSlide(currentIndex);
    });

    // Indicators
    document.querySelectorAll('.absolute.bottom-4 button').forEach((btn, i) => {
        btn.addEventListener('click', () => goToSlide(i));
    });

    // Auto-advance (optional)
    setInterval(() => {
        currentIndex = (currentIndex + 1) % slideCount;
        goToSlide(currentIndex);
    }, 6000);

    // ========================== accordion js =====================================
    // =============================================================================
    document.querySelectorAll('.accordion-toggle').forEach(button => {
        button.addEventListener('click', () => {
            const accordionContent = button.nextElementSibling;
            const isOpen = button.parentElement.classList.toggle('active');

            if (isOpen) {
                accordionContent.style.maxHeight = accordionContent.scrollHeight + 'px';
                setTimeout(() => {
                    accordionContent.style.opacity = '1';
                }, 10);
            } else {
                accordionContent.style.maxHeight = '0';
                accordionContent.style.opacity = '0';
            }
        });
    });
});