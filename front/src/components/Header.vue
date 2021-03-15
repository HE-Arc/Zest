<template>
  <v-app-bar app color="primary" dark>
    <router-link to="/">
      <div class="d-flex align-center">
        <img :src="require('./../assets/logo.svg')" height="42" class="my-3" />
        <h1 class="ml-3">Zest</h1>
      </div>
    </router-link>

    <v-spacer></v-spacer>

    <!-- Logged in -->
    <div v-if="this.$store.getters.isLoggedIn">
      <!-- Profile -->
      <v-btn to="/Home" class="mx-1 px-sm-1" text>
        <span class="hidden-md-and-down mr-2">Find resource</span>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <!-- Profile -->
      <v-btn to="/Profile" class="mx-1 px-sm-1" text>
        <span class="hidden-md-and-down mr-2">Profil</span>
        <v-icon>mdi-account-circle</v-icon>
      </v-btn>

      <!-- Login -->
      <v-btn to="/Logout" class="mx-1 px-sm-1" text>
        <span class="hidden-md-and-down mr-2">Logout</span>
        <v-icon>mdi-power</v-icon>
      </v-btn>
    </div>

    <!-- Not logged in -->
    <div v-if="!this.$store.getters.isLoggedIn">
      <v-btn to="/Login" class="mx-1 px-sm-1" text>
        <span class="hidden-md-and-down mr-2">Login</span>
        <v-icon>mdi-account-key</v-icon>
      </v-btn>
    </div>
  </v-app-bar>
</template>

<!-- SCRIPT -->
<script lang="js">
import Vue from "vue";
export default Vue.extend({
    name: "Header",
    methods: {
        //
    }
});
</script>