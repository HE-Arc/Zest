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
  props: {
    resource_id: null,
  },
  async beforeMount() {
      Api.get("ressources/"+this.resource_id).then((data) => {
          console.log(data);
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