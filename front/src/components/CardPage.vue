<template>
  <v-container fill-height fluid class="pa-0 background-gradient card-page">
    <v-row align="center" justify="center">
      <v-col align="center">
        <v-card class="mx-auto" max-width="450">
          <v-card-title class="primary white--text">
            <span class="title">{{this.title}}</span>
          </v-card-title>
          <div class="d-flex justify-center align-center my-5">
            <img :src="require('../assets/logo.svg')" height="92" />
            <div class="d-flex ml-2 card-header">
              <h1 class="mb-1">Zest</h1>
              <h2>your shared resources manager</h2>
            </div>
          </div>
          <slot></slot>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "CardPage",

  props: {
    title: String
  }
};
</script>
