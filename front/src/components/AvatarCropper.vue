<!-- TEMPLATE -->
<template>
  <div class="d-flex user">
    <img v-if="useImageAvatar()" :src="getAvatar()" />
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
      @uploaded="handleUploaded"
      @changed="changeFile"
      requestMethod="PATCH"
      :labels="labels"
      trigger="#pick-avatar"
      upload-form-name="picture"
      :upload-headers="headers"
      :upload-url="getApiUrl()"
      :output-mime="outputType"
    />
  </div>
</template>


<!-- SCRIPT -->
<script lang="ts">
import Vue from "vue";
import Api from "../logic/api/ApiRequester";
import AvatarCropper from "vue-avatar-cropper";

export default Vue.extend({
  created: function () {
    this.url = this.imgUrl;
  },
  components: { AvatarCropper },
  props: {
    fullname: String,
    size: {
      type: String,
      default: "40",
    },
  },
  data() {
    return {
      img: this.$store.getters.avatar,
      outputType: null,
      labels: {
        submit: "Submit",
        cancel: "Cancel",
      },
      headers: {
        Authorization: `Bearer ${Api.token}`,
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
    useImageAvatar: function () {
      return this.$store.getters.avatar != null;
    },
    getApiUrl: function () {
      return `${Api.getUrl()}users/profile`;
    },
    getAvatar: function () {
      return this.$store.getters.avatar;
    },
    changeFile(file) {
      this.outputType = file.type;
    },
    handleUploaded(response) {
      this.$store.dispatch("uploadAvatar", { avatar: response.picture.substring(1) });
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