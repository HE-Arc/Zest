<template>
  <ResourceDetail :resource="resource" />
</template>

<script lang="js">
import Vue from "vue";
import Api from "../logic/api/ApiRequester";
import ResourceDetail from "../components/ResourceDetail"

export default Vue.extend({
  name: "ResourceUpdate",
  components: {
    ResourceDetail
  },
  async beforeMount() {
      Api.get("ressources/"+this.$route.params.share_id).then((data) => {
          this.resource = data;
      });
  },
  data: function () {
    return {
      resource: undefined
    };
  }
});
</script>