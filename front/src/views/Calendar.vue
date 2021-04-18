<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="8" sm="6">
        <div class="text-center section">
          <h2>Calendar for {{ this.resource.name }}</h2>
          <div>
            <v-sheet tile class="d-flex">
              <v-toolbar flat>
                <v-btn icon class="ma-2" @click="$refs.calendar.prev()">
                  <v-icon>mdi-chevron-left</v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-toolbar-title v-if="$refs.calendar">{{
                  $refs.calendar.title
                }}</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-select
                  v-model="type"
                  :items="types"
                  dense
                  outlined
                  hide-details
                  label="type"
                ></v-select>

                <v-spacer></v-spacer>
                <v-btn icon class="ma-2" @click="$refs.calendar.next()">
                  <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
              </v-toolbar>
            </v-sheet>
            <v-sheet height="500">
              <v-calendar
                ref="calendar"
                v-model="calendar"
                :weekdays="weekday"
                :type="type"
                :events="events"
                :event-overlap-threshold="30"
                @click:event="showEvent"
                @click:more="viewDay"
                @click:date="viewDay"
                color="green darken-1"
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
                      color="primary"
                      @click="selectedOpen = false"
                      outlined
                    >
                      Cancel
                    </v-btn>
                    <v-btn
                      v-if="
                        this.$store.getters.userId == this.selectedEvent.userId
                      "
                      color="red darken-1"
                      @click="deleteEvent(selectedEvent)"
                    >
                      Delete
                    </v-btn>
                    <v-btn
                      v-else
                      disabled
                      color="red darken-1"
                      @click="deleteEvent(selectedEvent)"
                    >
                      Delete
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-menu>
            </v-sheet>
            <v-snackbar v-model="snackbar" :timeout="timeout">
              {{ infoText }}
              <template v-slot:action="{ attrs }">
                <v-btn
                  color="primary"
                  text
                  v-bind="attrs"
                  @click="snackbar = false"
                >
                  Close
                </v-btn>
              </template>
            </v-snackbar>
          </div>
        </div>
      </v-col>
      <v-col cols="6" sm="4" align-self="center">
        <v-card outlined>
          <v-card-title> Add new booking </v-card-title>
          <v-card-text> Select a date range and click save </v-card-text>
          <v-container>
            <v-spacer></v-spacer>
            <date-picker
              v-model="range"
              mode="dateTime"
              is24hr
              is-range
              color="green"
              :minute-increment="5"
            >
              <template v-slot="{ inputValue, inputEvents }">
                <form>
                  <v-text-field
                    prepend-icon="mdi-calendar"
                    label="Start date"
                    :value="inputValue.start"
                    v-on="inputEvents.start"
                  ></v-text-field>
                  <v-text-field
                    prepend-icon="mdi-calendar"
                    label="End date"
                    :value="inputValue.end"
                    v-on="inputEvents.end"
                  ></v-text-field>
                  <v-btn color="primary" outlined text @click="addEvent">
                    Save
                  </v-btn>
                </form>
              </template>
            </date-picker>
            <v-spacer></v-spacer>
          </v-container>
        </v-card>
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
      this.calendar = date
      this.type = 'day'
    },
    showEvent({nativeEvent, event}){
      const open = () => {
        this.selectedEvent = event
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
        user : parseInt(this.$store.getters.userId)
      }

      Api.post("ressources/"+this.$route.params.share_id+"/bookings", booking).then((data) => {
        this.events.push({
          id: data.id,
          userId: data.user,
          name: this.$store.state.user.username,
          start: new Date(this.range.start),
          end: new Date(this.range.end),
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          timed: true
        })
      })
    },
    deleteEvent(event){
      this.selectedOpen = false
      if(event.userId == this.$store.getters.userId){
        Api.delete("ressources/"+this.$route.params.share_id+"/bookings/"+event.id)
        this.infoText = "Bookig deleted"
        this.events.splice(this.events.indexOf(event), 1)
      }else{
        this.infoText = "Can't delete booking"
      }
      this.snackbar = true
    },
    rnd (a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
  },
  async beforeMount() {
    Api.get("ressources/"+this.$route.params.share_id).then((data) => {
        this.resource = data;
        this.resource.bookings.forEach(element => {
          let date_start = new Date(element.date_start)
          let date_end = new Date(element.date_end)
          this.events.push({
            id: element.id,
            userId: element.user.id,
            name: element.user.username,
            start: date_start,
            end: date_end,
            color: this.colors[this.rnd(0, this.colors.length - 1)],
            timed: true
          })
        });
    });
  },
  data: () => ({
      resource: {},
      range: {
        start: new Date(),
        end: new Date()
      },
      type: 'month',
      types: ['month', 'week', 'day'],
      weekday: [1, 2, 3, 4, 5, 6, 0],
      calendar: '',
      events: [],
      selectedEvent: {},
      selectedElement: null,
      selectedOpen: false,
      colors: [
                'pink darken-4',
                'blue', 
                'yellow darken-4', 
                'light-green lighten-3', 
                'green darken-2', 
                'teal darken-3', 
                'cyan accent-3', 
                'indigo', 
                'light-blue darken-4', 
                'deep-purple', 
                'cyan', 
                'green', 
                'orange', 
                'grey darken-1'
              ],
      infoText: '',
      timeout: '1000',
      snackbar: false,
    })
});
</script>