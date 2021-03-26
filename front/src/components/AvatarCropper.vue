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
    <v-icon id="pick-avatar" class="icon primary white--text"
      >mdi-upload</v-icon
    >

    <avatar-cropper
      @uploading="handleUploading"
      @uploaded="handleUploaded"
      @completed="handleCompleted"
      @error="handlerError"
      requestMethod="PATCH"
      :labels="labels"
      trigger="#pick-avatar"
      upload-url="/upload/image"
    />
  </div>
</template>


<!-- SCRIPT -->
<script lang="ts">
import Vue from "vue";
import Api from "../logic/api/ApiRequester";
import AvatarCropper from "vue-avatar-cropper";

export default Vue.extend({
  components: { AvatarCropper },
  props: {
    imgUrl: String,
    fullname: String,
    size: {
      type: String,
      default: "40",
    },
  },
  data() {
    return {
      labels: {
        submit: "Submit",
        cancel: "Cancel",
      },
    };
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
    handleUploading(form, xhr) {
      console.log(form, xhr);
      //this.message = "uploading...";
    },
    handleUploaded(response) {
      console.log(response);
      if (response.status == "success") {
        this.user.avatar = response.url;
        // Maybe you need call vuex action to
        // update user avatar, for example:
        // this.$dispatch('updateUser', {avatar: response.url})
        //this.message = "user avatar updated.";
      }
    },
    handleCompleted(response, form, xhr) {
      console.log(form, xhr, response);
      //this.message = "upload completed.";
    },
    handlerError(message, type, xhr) {
      console.log(message, type, xhr);
      //this.message = "Oops! Something went wrong...";
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