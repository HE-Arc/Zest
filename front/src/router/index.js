import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import SignUp from "../views/SignUp.vue";
import Logout from "../views/Logout.vue";
import Profile from "../views/Profile.vue";
import store from "../store";
import Api from "../logic/api/ApiRequester";
import Calendar from "../views/Calendar.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: {
      onlyUnlogged: true,
    },
  },
  {
    path: "/signUp",
    name: "SignUp",
    component: SignUp,
    meta: {
      onlyUnlogged: true,
    },
  },
  {
    path: '/resources/new',
    name: 'resources_new',
    component: () => import('../views/ResourceNew.vue'),
    meta: {
      onlyLogged: true,
    },
  },
  {
    path: '/resources/:resource_id/edit',
    name: 'resources_edit',
    props: true,
    component: () => import('../views/ResourceEdit.vue'),
    meta: {
      onlyLogged: true,
    },
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
    meta: {
      onlyLogged: true,
    },
  },
  {
    path: "/logout",
    name: "Logout",
    component: Logout,
    meta: {
      onlyLogged: true,
    }
  },
  {
    path: "/resources/:share_id",
    name: "Calendar",
    component: Calendar
  }
];

/**
 * Get session from sessionStorage if user reload page
 *
 * @author Lucas Fridez <lucas.fridez@he-arc.ch>
 * @return {*}  {boolean} true if session stored in sessionStorage; false otherwise
 */
function loadSessionFromStorage() {
  if (window.sessionStorage.getItem("user") != null) {
    const user = JSON.parse(window.sessionStorage.getItem("user") ?? "");
    const token = window.sessionStorage.getItem("token") ?? "";
    Api.setToken(token);
    store.dispatch("login", { token: token, user: user });
    return true;
  } else {
    return false;
  }
}

/**
 * Define is user is logged in Vuex ou sessionStorage
 *
 * @author Lucas Fridez <lucas.fridez@he-arc.ch>
 * @return {*}  {boolean} treue if user is logged in; false otherwise
 */
function isLogged() {
  // Not connected by login action
  if (!store.getters.isLoggedIn) {
    if (loadSessionFromStorage()) {
      return true;
    }
    return false;
  }
  return true;
}

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  const isLoggedIn = isLogged();
  if (to.matched.some((route) => route.meta.onlyLogged)) {
    if (!isLoggedIn) {
      next({ name: "Login" });
    } else {
      next();
    }
  } else if (to.matched.some((route) => route.meta.onlyUnlogged)) {
    if (isLoggedIn) {
      next({ name: "Home" });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
