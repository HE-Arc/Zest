<template>
  <v-container
    id="share-page"
    fill-height
    fill-width
    fluid
    class="background-accent-gradient d-flex align-center justify-center flex-col flex-col"
  >
    <h2><span class="fw-700">Z</span>est your life</h2>
    <div class="d-flex nowrap align-center justify-center">
      <v-text-field
        prepend-icon="mdi-magnify"
        type="text"
        solo
        label="Do you want to share a resource ?"
        class="mx-2 input-share"
      />
      <v-btn elevation="4" x-large class="primary my-3">Create</v-btn>
    </div>
    <Resource title="My resource" id="1" authorName="Lucas Fridez" authorAvatar="" nbTasks="2"/>
  </v-container>
</template>

<script lang="js">
import Vue from "vue";

import Resource from "../components/Resource";

export default Vue.extend({
    name: "Home",
    components: {Resource},
    methods: {
        //
    },
    data() {
        return {
            //
        };
    }
});
</script>
