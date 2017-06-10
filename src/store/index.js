import Vue from 'vue';
import Vuex from 'vuex';
import anime from './modules/anime';
import cg from './modules/cg';
import torrent from './modules/torrent';
import shortvideo from './modules/shortvideo';

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== 'production';

export default new Vuex.Store({
  modules: {
    anime, cg, torrent, shortvideo,
  },
  strict: debug,
});
