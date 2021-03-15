<template>
  <v-app class="v-application">
    <Header/>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import "./assets/styles/main.scss";

import Header from "./components/Header"

export default {
  name: "App",

  components: {Header},

  data: () => ({
    //
  }),
};
</script>
