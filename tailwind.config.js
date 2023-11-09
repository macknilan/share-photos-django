/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './share_photos_dj/templates/**/*.{html, js}',
      // './share_photos_dj/static/js/*.js',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
      require('flowbite/plugin')
  ],
}

