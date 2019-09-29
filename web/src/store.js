import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    mapCenter: {},
    showMapModal: false
  },
  mutations: {
    changeMapCenter(state, payload) {
      state.mapCenter = payload.center;
    },
    changeShowMapModal(state) {
      state.showMapModal = !state.showMapModal;
    }
  },
  actions: {}
});
