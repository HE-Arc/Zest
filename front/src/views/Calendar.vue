<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="8" sm="6">
        <div class="text-center section">
          <h2>Calendars for {{ this.resource.name }}</h2>
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
                @click:event="showEvent"
                @click:more="viewDay"
                @click:date="viewDay"
              >
              </v-calendar>
              <v-menu
                max-width="200px"
                v-model="selectedOpen"
                :close-on-content-click="false"
                :activator="selectedElement"
                offset-x
              >
                <v-card color="grey lighten-4" max-width="200px" flat>
                  <v-toolbar :color="selectedEvent.color" dark>
                    <v-toolbar-title
                      v-html="selectedEvent.name"
                    ></v-toolbar-title>
                    <v-spacer></v-spacer>
                  </v-toolbar>
                  <v-card-text>
                    <span v-html="selectedEvent.details"></span>
                  </v-card-text>
                  <v-card-actions>
                    <v-btn
                      text
                      color="grey darken-1"
                      @click="selectedOpen = false"
                    >
                      Cancel
                    </v-btn>
                    <v-btn color="red" @click="deleteEvent(selectedEvent)">
                      Delete
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-menu>
            </v-sheet>
          </div>
        </div>
      </v-col>
      <v-col cols="6" sm="4">
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
            <v-col cols="12" sm="6" md="4">
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
        <v-btn color="primary" text @click="addEvent"> Save </v-btn>
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
    viewDay({ date }){
      this.value = date
      this.type = 'day'
    },
    showEvent({nativeEvent, event}){
      const open = () => {
        this.selectedEvent = event
        console.log(this.selectedEvent)
        this.selectedElement = nativeEvent.target
        setTimeout(() => {
          this.selectedOpen = true
        }, 10)
      }

      if (this.selectedOpen) {
        this.selectedOpen = false
        setTimeout(open, 10)
      } else {
        open()
      }

      nativeEvent.stopPropagation()
    },
    addEvent(){
      let booking = {
        date_start : this.range.start,
        date_end : this.range.end,
        user : parseInt(this.$store.getters.userId),
        ressource : 1
      }
      Api.post("ressources/"+this.$route.params.resource_id+"/bookings", booking).then((data) => {
        this.events.push({
          id: data.id,
          name: this.name,
          start: this.range.start,
          end: this.range.end,
          color: this.colors[2]
        })
      })
    },
    deleteEvent(event){
      this.selectedOpen = false
      let eventIndex = this.events.indexOf(event)
      this.events.splice(eventIndex, 1)
      Api.delete("ressources/1/bookings/"+event.id)
    },
    rnd (a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
  },
  async beforeMount() {
    Api.get("ressources/"+this.$route.params.resource_id).then((data) => {
        this.resource = data;
        this.resource.bookings.forEach(element => {
          let date_start = new Date(element.date_start)
          let date_end = new Date(element.date_end)
          this.events.push({
            id: element.id,
            name: element.user.username,
            start: date_start,
            end: date_end,
            color: this.colors[this.rnd(0, this.colors.length - 1)]
          })
        });
    });
  },
  data: () => ({
      resource: {},
      name,
      range: {
        start: new Date(),
        end: new Date()
      },
      type: 'month',
      types: ['month', 'week', 'day', '4day'],
      weekday: [0, 1, 2, 3, 4, 5, 6],
      value: '',
      events: [],
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1']
    })
});
</script>