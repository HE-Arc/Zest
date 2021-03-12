<template>
  <v-container fill-height fluid grid-list-xl>
    <v-layout justify-center wrap>
      <v-flex xs12 md8>
        <TitledCard title="My resources">
          <v-form>
            <v-container py-0>
              <v-layout wrap>
                <p class="mt-4">
                  Below appears all of your resources ! Have a look at them and
                  maybe you can share another one !
                </p>
                <v-row class="mb-2">
                  <v-col
                    sm="12"
                    md="6"
                    lg="6"
                    xl="4"
                    v-for="i in Array.from(Array(5).keys())"
                    :key="i"
                  >
                    <Resource
                      :title="'Caquelon ' + (i + 1)"
                      authorName="Lucas Fridez"
                      :nbPeople="10 - i"
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
              Fridez Lucas
            </h3>
            <p class="card-description font-weight-light text-center">
              You need to change personnal information ? The form below can help
              you !
            </p>
            <v-form class="text-center">
              <v-text-field
                label="Name"
                prepend-icon="mdi-card-account-details"
                class="my-5"
              />
              <v-text-field
                label="Firstname"
                prepend-icon="mdi-account-circle"
                class="my-5"
              />
              <v-text-field
                label="Email"
                prepend-icon="mdi-email"
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
                rounded
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
import TitledCard from "../components/TitledCard"
import Resource from "../components/Resource"
import Avatar from "../components/Avatar"

export default Vue.extend({
    name: "Home",
    components: {TitledCard, Avatar, Resource},
    methods: {
        //
    },
    data() {
        return {
            //
        };
    }
});
</script>
