<template>
  <v-container fill-height fluid grid-list-xl>
    <v-layout justify-center wrap>
      <v-flex xs12 md8>
        <TitledCard
          color="general"
          title="Edit Profile"
          text="Complete your profile"
        >
          <v-form>
            <v-container py-0>
              <v-layout wrap>
                <v-flex xs12 md4>
                  <v-text-field label="Company (disabled)" disabled />
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field class="purple-input" label="User Name" />
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </TitledCard>
      </v-flex>
      <v-flex xs12 md4>
        <TitledCard class="v-card-profile">
          <Avatar slot="offset" class="mx-auto d-block" fullname="Lucas Fridez" size="130">
          </Avatar>
          <v-card-text class="text-xs-center">
            <h3 class="card-title font-weight-light text-center">Fridez Lucas</h3>
            <p class="card-description font-weight-light">
              You wrote that yourself? wow congrats dude, really, that's very
              cool. i just told everyone in my family about it, everybody thinks
              that's very impressive and asked me to congratulate you. they want
              to speak to you in person, if possible, to give you their regards.
              they also said they will tell our distant relatives that can make
              your name stand out more and see which city can congratulate you
              the hardest for this magnificent feat.
            </p>
          </v-card-text>
        </TitledCard>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="js">
import Vue from "vue";
import TitledCard from "../components/TitledCard"
import Avatar from "../components/Avatar"

export default Vue.extend({
    name: "Home",
    components: {TitledCard, Avatar},
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
