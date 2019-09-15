import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/Bus",
      name: "Bus",
      component: () => import("./views/Bus.vue")
    }
  ]
});
