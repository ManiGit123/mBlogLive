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
    const slideCount = document.querySelectorAll('.carousal-count').length;   //min-w-full
    let currentIndex = 0;

    function goToSlide(index) {
        // console.log(index)
        currentIndex = index;
        slides.style.transform = `translateX(-${currentIndex * 100}%)`;

        // Update indicators
        document.querySelectorAll('.absolute.bottom-4 button').forEach((btn, i) => {
            btn.classList.toggle('bg-white/80', i === currentIndex);
            btn.classList.toggle('bg-white/50', i !== currentIndex);
        });
    }

    // Next slide
    const next = document.querySelector('.absolute.right-4')
    next?.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % slideCount;
        goToSlide(currentIndex);
    });

    // Previous slide
    const previous = document.querySelector('.absolute.left-4')
    previous?.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + slideCount) % slideCount;
        goToSlide(currentIndex);
    });

    // Indicators
    const indicators = document.querySelectorAll('.absolute.bottom-4 button')
    indicators?.forEach((btn, i) => {
        btn.addEventListener('click', () => goToSlide(i));
    });

    // Auto-advance (optional)
    if (slideCount > 1) {
        setInterval(() => {
            currentIndex = (currentIndex + 1) % slideCount;
            goToSlide(currentIndex);
        }, 6000);
    }
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

    document.addEventListener('click', function (e) {
        const button = e.target.closest('.acc-expandable');
        if (button) {
            const targetId = button.getAttribute('data-target');
            const iconId = button.getAttribute('data-icon');
            const content = document.getElementById(targetId);
            const icon = document.getElementById(iconId);

            // SVG for Minus icon
            const minusSVG = `
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4">
            <path d="M3.75 7.25a.75.75 0 0 0 0 1.5h8.5a.75.75 0 0 0 0-1.5h-8.5Z" />
            </svg>
            `;

            // SVG for Plus icon
            const plusSVG = `
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4">
            <path d="M8.75 3.75a.75.75 0 0 0-1.5 0v3.5h-3.5a.75.75 0 0 0 0 1.5h3.5v3.5a.75.75 0 0 0 1.5 0v-3.5h3.5a.75.75 0 0 0 0-1.5h-3.5v-3.5Z" />
            </svg>
            `;

            if (content.style.maxHeight && content.style.maxHeight !== '0px') {
                content.style.maxHeight = '0';
                icon.innerHTML = plusSVG;
            } else {
                content.style.maxHeight = content.scrollHeight + 'px';
                icon.innerHTML = minusSVG;
            }
        }
    });

    // ========================== wagtail-codeblock js =====================================
    // =====================================================================================
    document.querySelectorAll('.custom-code-block .copy-button').forEach(button => {
        button.addEventListener('click', function () {
            const codeBlock = this.closest('.custom-code-block').querySelector('pre code');
            const buttonTextSpan = this.querySelector('.button-text'); // Get the span element

            navigator.clipboard.writeText(codeBlock.textContent).then(() => {
                if (buttonTextSpan) { // Make sure the span exists
                    buttonTextSpan.textContent = 'Copied!';
                }
                // You can also change the icon here if you want a "check" icon temporarily
                const icon = this.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-copy'); // Remove copy icon
                    icon.classList.add('fa-check'); // Add check icon
                }

                setTimeout(() => {
                    if (buttonTextSpan) {
                        buttonTextSpan.textContent = 'Copy';
                    }
                    if (icon) {
                        icon.classList.remove('fa-check'); // Remove check icon
                        icon.classList.add('fa-copy'); // Bring back copy icon
                    }
                }, 2000);
            });
        });
    });

    // Single event delegation for all download buttons
    document.addEventListener('click', function (e) {
        const button = e.target.closest('.download-button');
        if (button) {
            const codeId = button.getAttribute('data-target');
            const filename = button.getAttribute('data-filename');
            const codeBlock = document.getElementById(codeId);
            const buttonTextSpan = button.querySelector('.button-text');
            const icon = button.querySelector('i');

            // Dynamically get the file extension from the code block's data attribute
            if (filename?.includes("python")) {
                var fileExtension = "py";
            } else if (filename?.includes("html")) {
                var fileExtension = "html";
            } else if (filename?.includes("javascript")) {
                var fileExtension = "js";
            } else {
                var fileExtension = "txt";
            }
            const filenameExt = `${filename}.${fileExtension || 'txt'}`
            if (codeBlock) {
                const codeContent = codeBlock.textContent;
                const blob = new Blob([codeContent], { type: 'text/plain' });
                const url = URL.createObjectURL(blob);

                const a = document.createElement('a');
                a.href = url;
                a.download = filenameExt;
                document.body.appendChild(a);
                a.click();
                // Provide "Downloaded!" feedback
                if (buttonTextSpan) {
                    buttonTextSpan.textContent = 'Downloading...';
                }
                if (icon) {
                    icon.classList.remove('fa-download');
                    // icon.classList.add('fa-check'); // Change to checkmark icon
                    icon.classList.add('fa-spinner', 'fa-spin');
                }
                // Clean up and reset button state after a short delay
                setTimeout(() => {
                    if (buttonTextSpan) {
                        buttonTextSpan.textContent = 'Downloaded!'; // Reset text
                    }
                    if (icon) {
                        icon.classList.remove('fa-spinner', 'fa-spin');
                        icon.classList.add('fa-check'); // add checkmark
                        // icon.classList.add('fa-download'); // Reset to download icon
                    }
                }, 1000); // Display "Downloaded!" for 2 seconds

                // Clean up and reset button state after a short delay
                setTimeout(() => {
                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);

                    if (buttonTextSpan) {
                        buttonTextSpan.textContent = 'Download'; // Reset text
                    }
                    if (icon) {
                        // icon.classList.remove('fa-spinner', 'fa-spin');
                        icon.classList.remove('fa-check'); // Remove checkmark
                        icon.classList.add('fa-download'); // Reset to download icon
                    }
                }, 3000); // Display "Downloaded!" for 2 seconds
            }
        }
    });

    // ========================== Social media share js =====================================
    // =====================================================================================
    // Get all share buttons on the page
    const shareButtons = document.querySelectorAll('[id^="shareIcon-"]');

    shareButtons.forEach(shareButton => {
        // Extract the ID number from the button ID
        const elementId = shareButton.id.split('-')[1];
        const socialIconsPopup = document.getElementById(`socialIconsPopup-${elementId}`);

        if (socialIconsPopup) {
            shareButton.addEventListener('click', function (e) {
                e.stopPropagation(); // Prevent immediate document click handler
                console.log(`Social clicked for element ${elementId}`);
                socialIconsPopup.classList.toggle('show');
            });
        }
    });

    // Close any open popups when clicking outside
    document.addEventListener('click', function (event) {
        const allPopups = document.querySelectorAll('.social-icons-popup.show');
        allPopups.forEach(popup => {
            const elementId = popup.id.split('-')[1];
            const shareButton = document.getElementById(`shareIcon-${elementId}`);

            if (!popup.contains(event.target) && (!shareButton || !shareButton.contains(event.target))) {
                popup.classList.remove('show');
            }
        });
    });

});