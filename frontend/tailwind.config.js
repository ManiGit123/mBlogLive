const plugin = require('tailwindcss/plugin');

//** @type {import('tailwindcss').Config} */

export default {
    content: ["./src/**/*.{html,js}", "../templates/**/*.html", "../../mBlogLive/**/*.html"],
    darkMode: 'class', //
    theme: {
        extend: {
            // You can define custom colors here if needed, as in previous chats
            colors: {
                'primary': {
                    DEFAULT: '#007bff',
                    'dark': '#66a3ff',
                },
                'background-light': '#f4f4f4',
                'background-dark': '#1a202c',
                'card-bg-light': '#ffffff',
                'card-bg-dark': '#2d3748',
                'text-light': '#333',
                'text-dark': '#e2e8f0',
            },

            // This is where you configure the default 'container' behavior
            container: {
                center: true, // This centers the container horizontally
                padding: {
                    DEFAULT: '1rem', // Default padding for small screens
                    sm: '1.25rem',   // Padding for small screens and up (if you want responsive padding)
                    lg: '2rem',      // Padding for large screens and up
                    xl: '2.5rem',    // Padding for extra large screens and up
                },
                // You can define custom breakpoints here if you want to exactly match Bootstrap's
                // Tailwind's default breakpoints are slightly different:
                // sm: 640px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1536px
                // Bootstrap's are:
                // sm: 576px, md: 768px, lg: 992px, xl: 1200px, xxl: 1400px
                // screens: {
                //   sm: '576px',
                //   md: '768px',
                //   lg: '992px',
                //   xl: '1200px',
                //   '2xl': '1400px', // or 'xxl' if you prefer, then use 'max-w-xxl' in CSS
                // },
            },
        },
        plugins: [
        ],
        // prefix: 'tw'
    }
}

// @import "tailwindcss" prefix(tw);
// @source "../../templates/**/*.html";
// @source "../../myappNodeJs/**/templates/**/*.html";

// @layer base {

//     *,
//     *:: before,
//     *::after {
//         box - sizing: border - box;
//     }

//     * {
//         margin: 0;
//         padding: 0;
//     }

//     html {
//         font - family: sans - serif;
//         color: #333;
//     }
// }


// /* Custom Header Styles using @apply */
// h1 {
//     @apply text - 4xl font - bold mb - 4;
//     /* Adjust these values as needed */
// }

// h2 {
//     @apply text - 3xl font - semibold mb - 3;
// }

// h3 {
//     @apply text - 2xl font - medium mb - 2;
// }

// h4 {
//     @apply text - xl font - medium mb - 2;
// }

// h5 {
//     @apply text - lg font - medium mb - 1;
// }

// h6 {
//     @apply text - base font - normal mb - 1;
// }