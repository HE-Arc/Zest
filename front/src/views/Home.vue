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
        prepend-icon="mdi-calendar-plus"
        type="text"
        solo
        label="Do you want to share a resource ?"
        class="mx-2 input-share"
        v-model="name"
      />
      <v-btn elevation="4" x-large class="primary my-3" @click="goToCreate">Create</v-btn>
    </div>
  </v-container>
</template>

<script lang="js">
import Vue from "vue";

export default Vue.extend({
    name: "Home",
    components: {},
    methods: {
      goToCreate: function () {
        let queries = {};
        if (name != undefined) {
          queries.name = this.name;
        }
        this.$router.push({name: 'resources_new', query: queries});
      }
    },
    data() {
        return {
          name: undefined
        };
    }
});
</script>
