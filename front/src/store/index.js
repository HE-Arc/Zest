import Vue from "vue";
import Vuex from "vuex";
import Api from "./../logic/api/ApiRequester";

Vue.use(Vuex);

// https://pusher.com/tutorials/authentication-vue-vuex#set-up-vuex-actions
export default new Vuex.Store({
  state: {
    fullname: "Adam Smith",
    loggedIn: false,
    status: "",
    token: "",
  },
  mutations: {
    authenticationSuccess(state, token, user) {
      // TODO
    },
    authenticationError(state) {
      // TODO
    },
    logout(state) {
      state.token = "";
    },
  },
  actions: {
    login({ commit }, user) {
      // TODO
    },
    register({ commit }, user) {
      // TODO
    },
    logout({ commit }) {
      // TODO
    },
  },
  modules: {},
  getters: {
    isLoggedIn: (state) => !!state.token,
    authStatus: (state) => state.status,
  },
});
