<template>
  <ResourceDetail :resource="resource"/>
</template>

<script lang="js">
import Vue from "vue";
import ResourceDetail from "../components/ResourceDetail"

export default Vue.extend({
  name: "ResourceNew",
  components: {
    ResourceDetail
  },
    data: function () {
    return {
      resource: {
        name: this.$route.query.name,
        date_start : (new Date()).toISOString().substr(0, 10)
      }
    };
  }

});
</script>