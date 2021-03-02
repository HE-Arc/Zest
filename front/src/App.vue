<template>
  <v-app class="v-application">
    <v-app-bar app color="primary" dark>
        <router-link to="/">
      <div class="d-flex align-center">
          <img :src="require('./assets/logo.svg')" height="42" class="my-3" />
          <h1 class="ml-3">Zest</h1>
      </div>
        </router-link>

      <v-spacer></v-spacer>
      <router-link to="/" class="white--text">Home</router-link> |
      <router-link to="/Login" class="white--text">Login</router-link>
      <router-link to="/SignUp" class="white--text">SignUp</router-link>
      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import "./assets/styles/main.scss";

export default {
  name: "App",

  components: {},

  data: () => ({
    //
  }),
};
</script>
