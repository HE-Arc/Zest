<template>
  <v-container fill-height fluid class="pa-0 background-gradient card-page">
    <v-row align="center" justify="center">
      <v-col align="center">
        <v-card class="mx-auto" max-width="450">
          <v-card-title class="primary white--text">
            <span class="title">Login</span>
          </v-card-title>
          <v-card-text>
            <div class="d-flex justify-center align-center my-5">
              <img :src="require('../assets/logo.svg')" height="92" />
              <div class="d-flex ml-2 card-header">
                <h1 class="mb-1">Zest</h1>
                <h2>your shared resources manager</h2>
              </div>
            </div>
            <v-text-field
              label="Email"
              v-model="email"
              :disabled="loading"
              :rules="[rules.email]"
              prepend-icon="mdi-email"
              class="my-5"
            ></v-text-field>
            <v-spacer></v-spacer>
            <v-text-field
              :append-icon="showPassord ? 'mdi-eye' : 'mdi-eye-off'"
              prepend-icon="mdi-lock"
              :disabled="loading"
              :rules="[rules.required, rules.min]"
              :type="showPassord ? 'text' : 'password'"
              label="Password"
              v-model="password"
              class="my-5"
              @keydown.enter="login"
              @click:append="showPassord = !showPassord"
            ></v-text-field>
            <p v-if="errorPost.length > 0" class="red--text">{{ errorPost }}</p>
          </v-card-text>
          <v-btn
            elevation="4"
            x-large
            class="primary white--text my-3"
            large
            rounded
            :loading="loading"
            v-on:click="login"
            >Login</v-btn
          >
          <v-spacer></v-spacer>
          <v-btn to="/SignUp" text color="accent  mb-5 mt-0">
            Create an account
          </v-btn>
          <v-spacer></v-spacer>

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
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="js">
import Vue from "vue";
import Api from "../logic/api/ApiRequester";
import { ZestError } from "../logic/api/ZestError";
import { ZestError422 } from "../logic/api/ZestError422";

export default Vue.extend({
    name: "Login",
    methods: {
        login: async function () {
            this.loading = true;
            try {
                await Api.login({
                    email: this.email,
                    password: this.password
                });
                this.errorPost = "";
                this.$router.push({ name: "Workbooks" });
            } catch (e) {
                if (e instanceof ZestError422) {
                    console.log(e.data); // Errors with sent data
                } else if (e instanceof ZestError) {
                    this.errorPost = e.message; // Error (401, 404 or 500,...)
                }
            } finally {
                this.loading = false;
            }
        }
    },
    data() {
        return {
            loading: false,
            errorPost: "",
            password: "",
            email: "",
            showPassord: false,
            rules: {
                required: (value) => !!value || "Required",
                min: (v) => v.length >= 6 || "Minimum 6 characters",
                email: (value) => {
                    const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                    return pattern.test(value) || "Invalid e-mail.";
                }
            }
        };
    }
});
</script>