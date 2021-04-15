<template>
  <v-container fill-height fluid grid-list-xl>
    <v-layout justify-center wrap>
      <v-flex xs12 md8>
        <TitledCard title="My resources">
          <v-form>
            <v-container py-0>
              <v-layout wrap>
                <p class="mt-4 col-12">
                  Below appears all of your resources ! Have a look at them and
                  maybe you can share another one !
                </p>
                <v-row class="mb-2">
                  <v-col
                    sm="12"
                    md="6"
                    lg="6"
                    xl="4"
                    v-for="resource in resources"
                    :key="resource.id"
                  >
                    <Resource
                      :title="resource.name"
                      :authorName="resource.author.first_name + ' ' + resource.author.last_name"
                      :nbPeople="resource.participants.length"
                      :id="resource.share_id"
                    />
                  </v-col>
                </v-row>
              </v-layout>
            </v-container>
          </v-form>
        </TitledCard>
      </v-flex>
      <v-flex xs12 md4>
        <TitledCard class="v-card-profile">
          <Avatar
            slot="offset"
            class="mx-auto d-block"
            fullname="Lucas Fridez"
            size="130"
          >
          </Avatar>
          <v-card-text class="text-xs-center">
            <h3 class="card-title font-weight-light text-center mb-2">
              {{ lastname }} {{ firstname }}
            </h3>
            <p class="card-description font-weight-light text-center">
              You need to change personnal information ? The form below can help
              you !
            </p>
            <v-form class="text-center" v-model="isFormValid">
              <v-text-field
                label="Email"
                v-model="email"
                disabled
                prepend-icon="mdi-email"
                class="my-5"
              />
              <v-text-field
                label="Username"
                v-model="this.$store.state.user.username"
                disabled
                prepend-icon="mdi-account-details"
                class="my-5"
              />
              <v-text-field
                label="Name"
                v-model="lastname"
                :rules="[rules.required]"
                prepend-icon="mdi-card-account-details"
                class="my-5"
              />
              <v-text-field
                label="Firstname"
                v-model="firstname"
                :rules="[rules.required]"
                prepend-icon="mdi-account-circle"
                class="my-5"
              />
              <v-flex>
                <v-layout column align-center>
                  <v-switch
                    v-model="$vuetify.theme.dark"
                    inset
                    label="Dark Theme"
                    persistent-hint
                  ></v-switch>
                </v-layout>
              </v-flex>
              <v-btn
                elevation="4"
                x-large
                class="primary white--text my-3 mt-0 mb-5"
                large
                @click="updateProfile"
                rounded
                :disabled="!isFormValid"
                :loading="loading"
                >Update profile</v-btn
              >
            </v-form>
          </v-card-text>
        </TitledCard>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="js">
import Vue from "vue";
import Api from "../logic/api/ApiRequester";
import TitledCard from "../components/TitledCard"
import Resource from "../components/Resource"
import Avatar from "../components/AvatarCropper"

export default Vue.extend({
    name: "Home",
    components: {TitledCard, Avatar, Resource},
    async created() {
      this.resources = await Api.get("ressources");
      console.log(this.resources);
    },
    methods: {
        updateProfile: async function() {
          this.loading = true;
          await Api.patch("users/profile", {
              last_name: this.lastname,
              first_name: this.firstname,
          });
          this.loading = false;
        }
    },
    data() {
      return {
        firstname: this.$store.state.user.first_name,
        lastname: this.$store.state.user.last_name,
        email: this.$store.state.user.email,
        loading: false,
        resources: [],
        isFormValid: true,
        rules: {
          required: (value) => !!value || "Required",
        }
      };
    }
});
</script>
