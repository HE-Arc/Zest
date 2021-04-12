<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="6">
        <div class="text-center section">
          <h2>Calendars</h2>
          <div>
            <v-sheet tile height="54" class="d-flex">
              <v-btn icon class="ma-2" @click="$refs.calendar.prev()">
                <v-icon>mdi-chevron-left</v-icon>
              </v-btn>

              <v-spacer></v-spacer>
              <v-btn icon class="ma-2" @click="$refs.calendar.next()">
                <v-icon>mdi-chevron-right</v-icon>
              </v-btn>
            </v-sheet>
            <v-sheet height="500">
              <v-calendar
                ref="calendar"
                v-model="value"
                :weekdays="weekday"
                :type="type"
                :events="events"
                :event-overlap-threshold="30"
              ></v-calendar>
            </v-sheet>
          </div>
        </div>
      </v-col>
      <v-col cols="12" sm="6">
        <v-select
          v-model="type"
          :items="types"
          dense
          outlined
          hide-details
          class="ma-2"
          label="type"
        ></v-select>
        <v-divider></v-divider>
        <v-container>
          <v-row>
            <v-col cols="20" sm="6" md="4">
              <v-text-field
                label="Your name"
                v-model="name"
                required
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <date-picker
              v-model="range"
              mode="dateTime"
              is24hr
              is-range
              :minute-increment="5"
            >
              <template v-slot="{ inputValue, inputEvents }">
                <div>
                  <input :value="inputValue.start" v-on="inputEvents.start" />
                  <input :value="inputValue.end" v-on="inputEvents.end" />
                </div>
              </template>
            </date-picker>
          </v-row>
        </v-container>
        <v-btn color="primary" text @click="test"> Save </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="js">
import Vue from 'vue'
import Api from "../logic/api/ApiRequester"


export default Vue.extend({
  name: "Calendar",
  components: {
  },
  methods: {
   test(){
      this.events.push({
        name: this.name,
        start: this.range.start,
        end: this.range.end,
        color: this.colors[2]
      })
    }
  },
  async beforeMount() {
    Api.get("ressources/"+this.$route.params.resource_id).then((data) => {
        console.log(data);
        this.resource = data;
    });
  },
  data: () => ({
      resource: undefined,
      name,
      range: {
        start: new Date(),
        end: new Date()
      },
      type: 'month',
      types: ['month', 'week', 'day', '4day'],
      weekday: [0, 1, 2, 3, 4, 5, 6],
      weekdays: [
        { text: 'Sun - Sat', value: [0, 1, 2, 3, 4, 5, 6] },
        { text: 'Mon - Sun', value: [1, 2, 3, 4, 5, 6, 0] },
        { text: 'Mon - Fri', value: [1, 2, 3, 4, 5] },
        { text: 'Mon, Wed, Fri', value: [1, 3, 5] },
      ],
      value: '',
      events: [],
      colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1']
    }),
  computed: {
    //
  }
});
</script>