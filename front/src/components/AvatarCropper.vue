<!-- TEMPLATE -->
<template>
  <div class="d-flex user">
    <v-img v-if="imgUrl && imgUrl != 'user.jpg'" :src="getAvatar()" />
    <v-avatar
      v-else
      color="primary lighten-2 d-flex avatar-cropper"
      :size="size"
    >
      <span
        class="white--text headline text-center align-center justify-center profile-img"
        >{{ getInitials() }}</span
      >
    </v-avatar>
    <v-icon class="icon primary white--text" @click="$refs.FileInput.click()"
      >mdi-upload</v-icon
    >
  </div>
</template>


<!-- SCRIPT -->
<script lang="ts">
import Vue from "vue";
import Api from "../logic/api/ApiRequester";
export default Vue.extend({
  props: {
    imgUrl: String,
    fullname: String,
    size: {
      type: String,
      default: "40",
    },
  },
  methods: {
    getInitials: function () {
      if (this.fullname) {
        return this.fullname
          .match(/\b(\w)/g)
          .join("")
          .toUpperCase();
      } else {
        return "??";
      }
    },
    getAvatar: function () {
      return `${Api.getUrl()}storage/avatars/${this.imgUrl}`;
    },
  },
});
</script>
<style>
.user {
  justify-content: center;
  position: relative;
}
.profile-img {
  border-radius: 50%;
}

.v-application .primary.lighten-2.avatar-cropper {
  border: 3px solid var(--v-primary-base) !important;
}

.icon {
  position: absolute;
  top: 80px;
  right: 25px;
  border-radius: 100%;
  width: 30px;
  height: 30px;
  line-height: 30px;
  vertical-align: middle;
  text-align: center;
  font-size: 14px;
  cursor: pointer;
}
</style>