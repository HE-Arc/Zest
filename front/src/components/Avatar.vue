<!-- TEMPLATE -->
<template>
    <v-img v-if="imgUrl && imgUrl != 'user.jpg'" :src="getAvatar()" />
    <v-avatar v-else color="primary lighten-2 d-flex" :size="size">
        <span class="white--text headline text-center align-center justify-center">{{ getInitials() }}</span>
    </v-avatar>
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
            default: "40"
        }
    },
    methods: {
        getInitials: function () {
            if (this.fullname){
                return this.fullname
                    .match(/\b(\w)/g)
                    .join("")
                    .toUpperCase();
            }else{
                return "??";
            }
        },
        getAvatar: function() {
            return `${Api.getUrl()}storage/avatars/${this.imgUrl}`;
        }
    }
});
</script>