<template>
  <ResourceEdit ></ResourceEdit>
</template>

<script lang="js">
import Vue from "vue";
import ResourceEdit from "../components/ResourceEdit"

export default Vue.extend({
  name: "ResourceDetail",
  components: {
    ResourceEdit
  }

});
</script>