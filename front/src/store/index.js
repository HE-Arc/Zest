import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

// https://pusher.com/tutorials/authentication-vue-vuex#set-up-vuex-actions
export default new Vuex.Store({
  state: {
    loggedIn: false,
    status: "",
    token: "",
    user: null,
  },
  mutations: {
    authentication(state, { token, user }) {
      state.token = token;
      state.loggedIn = true;
      state.status = "loggedin";
      state.user = user;
    },
    updateAvatar(state, { avatar }) {
      state.user.picture = avatar;
    },
    logout(state) {
      state.token = "";
      state.loggedIn = false;
      state.status = "unlogged";
      state.user = null;
    },
  },
  actions: {
    login({ commit }, payload) {
      const user = payload.user;
      const token = payload.token;
      window.sessionStorage.setItem("user", JSON.stringify(user));
      window.sessionStorage.setItem("token", token);
      commit("authentication", { token, user });
    },
    logout({ commit }) {
      window.sessionStorage.removeItem("user");
      window.sessionStorage.removeItem("token");
      commit("logout");
    },
    uploadAvatar({ commit }, payload) {
      const avatar = payload.avatar;
      commit("updateAvatar", { avatar });
    },
  },
  modules: {},
  getters: {
    isLoggedIn: (state) => state.loggedIn,
    authStatus: (state) => state.status,
    fullname: (state) => `${state.user.last_name} ${state.user.first_name}`,
    avatar: (state) => state.user.picture,
  },
});
