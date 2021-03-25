<template>
    <v-container>
        <h2 v-if="resource.id">Update resource</h2>
        <h2 v-else>Create resource</h2>
        <form>
            <v-text-field v-model="resource.name" label="Name" :error-messages="nameErrors" required @input="$v.resource.name.$touch()" @blur="$v.resource.name.$touch()"></v-text-field>
            <v-layout row align-center wrap>
                <v-flex xs12 sm6 md4>
                    <date-picker :date.sync="resource.dateStart" :label="'From'"/>
                </v-flex>
                <v-flex xs12 sm6 md4>
                    <date-picker :date.sync="resource.dateEnd" :label="'To'"/>
                </v-flex>
            </v-layout>
            <v-textarea v-model="resource.description" label="Description"></v-textarea>
            
            <v-btn class="mr-4" @click="submit" v-if="resource.id">
                Update
            </v-btn>
            <v-btn class="mr-4" @click="submit" v-else>
                Create
            </v-btn>

        </form>
    </v-container>
</template>

<script lang="js">
import Vue from "vue";
import { validationMixin } from 'vuelidate'
import {
    required,
    minLength,
    maxLength
} from 'vuelidate/lib/validators'
import DatePicker from '../components/DatePicker'

export default Vue.extend({
  name: "ResourceEdit",
  mixins: [validationMixin],
  components: {
      DatePicker
  },
  props: {
    resource: {
        type: Object,
        default: function() {
            return {
                id: undefined,
                name: '',
                description: '',
                dateStart: (new Date()).toISOString().substr(0, 10),
                dateEnd: undefined,
            }
        }
    }
  },

  validations: {
      resource: {
          name: { required, minLength: minLength(4), maxLength: maxLength(255) },
      }
  },

  data: () => ({
  }),

  methods: {
    submit () {
      this.$v.$touch()
    },
    clear () {
      this.$v.$reset()
      this.id
    },
  },

  computed: {
    nameErrors () {
      const errors = []
      if (!this.$v.resource.name.$dirty) return errors
      !this.$v.resource.name.maxLength && errors.push('Name must be at most 255 characters long')
      !this.$v.resource.name.minLength && errors.push('Name must be at least 4 characters long')
      !this.$v.resource.name.required && errors.push('Name is required.')
      return errors
    },
  }
});
</script>