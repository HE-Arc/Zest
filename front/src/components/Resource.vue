<!-- TEMPLATE -->
<template>
    <v-card class="primary" elevation="4" v-on:click="goToResource(id)">
        <v-card-title class="white--text">{{ title }}</v-card-title>

        <v-card-actions>
            <v-list-item class="grow">
                <v-list-item-avatar color="grey darken-3">
                    <Avatar
                    :imgUrl="authorAvatar"
                    :fullname="authorName"
                    />
                </v-list-item-avatar>

                <v-list-item-content class="all-width">
                    <v-list-item-title class="white--text">{{ this.authorName }}</v-list-item-title>
                </v-list-item-content>

                <v-row align="center" justify="end">
                    <v-icon class="mr-1"> mdi-account-multiple </v-icon>
                    <span class="subheading">{{ this.nbPeople }}</span>
                </v-row>
            </v-list-item>
        </v-card-actions>
    </v-card>
</template>

§
<!-- SCRIPT -->
<script lang="ts">
import Vue from "vue";
import Avatar from "./Avatar.vue";
export default Vue.extend({
    components: {
        Avatar,
    },
    props: {
        title: String,
        id: String,
        authorName: String,
        authorAvatar: String,
        nbPeople: Number
    },
    data() {
        return {
            settings: []
        };
    },
    methods: {
        goToResource: function (id) {
            this.$router.push({ name: "Calendar", params: { share_id: id } });
        }
    }
});
</script>

<!--CSS-->
<style scoped>
.all-width {
    flex: 2;
}

.v-card__actions {
    padding-left: 0;
    padding-top: 0;
}
</style>