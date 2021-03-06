<template>
  <CardPage title="Sign Up">
    <v-form v-model="isFormValid">
      <v-card-text>
        <v-text-field
          label="Name"
          v-model="name"
          :disabled="loading"
          :rules="[rules.required]"
          prepend-icon="mdi-card-account-details"
          :error-messages="errors['name']"
          class="my-5"
        ></v-text-field>
        <v-text-field
          label="Firstname"
          v-model="firstname"
          :disabled="loading"
          :rules="[rules.required]"
          prepend-icon="mdi-account-circle"
          :error-messages="errors['firstname']"
          class="my-5"
        ></v-text-field>
        <v-text-field
          label="Username"
          v-model="username"
          :disabled="loading"
          :rules="[rules.required]"
          prepend-icon="mdi-account-details"
          :error-messages="errors['username']"
          class="my-5"
        ></v-text-field>
        <v-text-field
          label="Email"
          v-model="email"
          :disabled="loading"
          :rules="[rules.email]"
          prepend-icon="mdi-email"
          :error-messages="errors['email']"
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
          :error-messages="errors['password']"
          class="my-5"
          @click:append="showPassord = !showPassord"
        ></v-text-field>
      </v-card-text>
      <v-btn
        elevation="4"
        x-large
        class="primary white--text my-3 mt-0 mb-5"
        large
        rounded
        :loading="loading"
        v-on:click="signup"
        :disabled="!isFormValid && !alreadyTried"
        >Sign Up</v-btn
      >
      <v-spacer></v-spacer>
      <v-btn to="/Login" text color="primary mb-5 mt-0">
        I already have an account !
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
    </v-form>
  </CardPage>
</template>

<script lang="js">
import Vue from "vue";
import Api from "../logic/api/ApiRequester";
import CardPage from "../components/CardPage";
import { ZestError } from "../logic/api/ZestError";
import { ZestRegisterError } from "../logic/api/ZestRegisterError";

export default Vue.extend({
    name: "SignUp",
    components: {CardPage},
    methods: {
        signup: async function () {
            this.loading = true;
            try {
                await Api.register({
                    last_name: this.name,
                    first_name: this.firstname,
                    username: this.username,
                    email: this.email,
                    password: this.password
                });
                this.$router.push({name: "Home"});
            } catch (e) {
                if (e instanceof ZestRegisterError) {
                    const errors = e.message;
                    this.errors["username"] = errors.username.[0] ?? "";
                    this.errors["email"] = errors.email.[0] ?? "";
                    this.alreadyTried = true;
                    console.log(this.alreadyTried);
                } else if (e instanceof ZestError) {
                    console.log(e.message); // Error (401, 404 or 500,...)
                }
            } finally {
                this.loading = false;
            }
        }
    },
    data() {
        return {
            name: "",
            firstname: "",
            username: "",
            email: "",
            password: "",
            loading: false,
            showPassord: false,
            errors: {
                email: "",
                name: "",
                username: "",
                firstname: "",
                password: ""
            },
            isFormValid: false,
            alreadyTried: false,
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