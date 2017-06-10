import Vue from 'vue';
import Vuex from 'vuex';
import anime from './modules/anime';
import cg from './modules/cg';

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== 'production';

export default new Vuex.Store({
  modules: {
    anime, cg,
  },
  strict: debug,
});
