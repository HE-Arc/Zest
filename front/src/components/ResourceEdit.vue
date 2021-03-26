<template>
    <v-container>
        <h2 v-if="resource.id">Update resource</h2>
        <h2 v-else>Create resource</h2>
        <form>
            <v-text-field v-model="resource.name" label="Name" required @input="$v.resource.name.$touch()" @blur="$v.resource.name.$touch()"></v-text-field>
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
import DatePicker from '../components/DatePicker'

export default Vue.extend({
  name: "ResourceEdit",
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

});
</script>