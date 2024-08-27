module.exports = {
  content: [
    './index.html',
    './secondpage.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: ["dark"], // You can customize or add more themes here
  },
}

