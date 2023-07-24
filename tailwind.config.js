/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}", "./!(build|dist|.*)/**/*.{html,js}", "./**/**/*.{html,js}", "./Main/templates/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        red: "#fe3030",
        skyblue: "#30d9fe",
        powderblue: "#caecf3",
        darkslateblue: "#18264a",
        lightcyan: "#cfecea",
        btnlabel: "#fff",
        btnbkgnormal: "#000",
        gainsboro: "rgba(217, 217, 217, 0)",
      },
      fontFamily: {
        btnfont: "Roboto",
        b612: "B612",
        "button-text": "'Open Sans'",
      },
      borderRadius: {
        "3xs": "10px",
      },
    },
    fontSize: {
      lg: "18px",
      "10xl": "29px",
      mini: "15px",
      sm: "14px",
    },
  },
  corePlugins: {
    preflight: false,
  },
};
