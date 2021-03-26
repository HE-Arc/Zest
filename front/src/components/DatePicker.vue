<template>
  <v-container grid-list-md>
    <v-layout row wrap>
      <v-flex xs12>
        <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="false"
          :nudge-right="40"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on }">
            <v-text-field
              v-model="date"
              :label="label"
              persistent-hint
              prepend-icon="mdi-calendar"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date"
            locale="fr-ch"
            no-title
            @input="updateDate(date)"
          ></v-date-picker>
        </v-menu>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "DatePicker",
  props: {
    date: String,
    label: {
      type: String,
      default: "Date",
    },
  },
  data() {
    return {
      menu: false,
    };
  },
  methods: {
    updateDate() {
      this.menu = false;
      this.$emit("update:date", this.date);
    },
  }
};
</script>
