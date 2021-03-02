import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: {
      customProperties: true,
    },
    themes: {
      light: {
        primary: "#3f612d",
        secondary: "#f8f0c9",
        accent: "#9ca97b",
        error: "#b71c1c",
      },
      dark: {
        primary: "#3f612d",
        secondary: "#b0bec5",
        accent: "#e53935",
        error: "#e53935",
      },
    },
    dark: false,
  },
});
