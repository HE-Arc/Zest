<template>
  <v-container>
    <h2 v-if="resource.id">Update resource</h2>
    <h2 v-else>Create resource</h2>
    <form>
      <v-text-field
        v-model="resource.name"
        label="Name"
        required
        :rules="[rules.required, rules.min]"
      ></v-text-field>
      
      <v-file-input
        label="File input"
        filled
        prepend-icon="mdi-camera"
        v-model="imageUpload"
      ></v-file-input>
      <v-layout row align-center wrap>
        <v-flex xs12 sm6 md4>
          <date-picker :date.sync="resource.date_start" :label="'From'" />
        </v-flex>
        <v-flex xs12 sm6 md4>
          <date-picker :date.sync="resource.date_end" :label="'To'" />
        </v-flex>
      </v-layout>
      <v-textarea
        v-model="resource.description"
        label="Description"
        :rules="[rules.required]"
      ></v-textarea>

      <v-btn class="mr-4" @click="submitUpdate" v-if="resource.id">
        Update
      </v-btn>
      <v-btn class="mr-4" @click="submitCreate" v-else> Create </v-btn>
    </form>
  </v-container>
</template>

<script lang="js">
import Vue from "vue";
import Api from "../logic/api/ApiRequester";
import DatePicker from '../components/DatePicker'

export default Vue.extend({
  name: "ResourceDetail",
  components: {
      DatePicker
  },
  props: {
    resource: {
        type: Object,
        default: function() {
            return {
                id: undefined,
                picture: undefined,
                name: undefined,
                description: undefined,
                date_start: (new Date()).toISOString().substr(0, 10),
                date_end: undefined,
            }
        }
    }
  },

  data() {
      return {
        rules: {
            required: (value) => !!value || "Required",
            min: (v) => (v != undefined && v.length >= 4) || "Minimum 4 characters",
        },
        imageUpload: []
      }
  },
  

  methods: {
    _compileData(arr){
        let data = new FormData();
        for (let key in arr) {
            if (arr[key])
                data.append(key, arr[key]);
        }

        data.delete('picture');
        if (this.imageUpload) {
          data.append('picture', this.imageUpload)
        }
        
        return data;
    },
    async submitCreate () {
        let data = this._compileData(this.resource);
        try {
            await Api.post("ressources", data, {'Content-Type': 'multipart/form-data'});
            this.$router.push({ name: "Home" });
        } catch(e){
            console.log(e);
        }
    },
    async submitUpdate () {
        let data = this._compileData(this.resource);
        let router = this.$router;
        try {
            await Api.patch("ressources/" + this.resource.share_id, data, {'Content-Type': 'multipart/form-data'}).then(() => {
              router.go();
            });
            //
        } catch(e){
            console.log(e);
        }
    }
  }
});
</script>