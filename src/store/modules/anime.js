import axios from 'axios';

const state = {
  isFetching: false,
  data: [],
};

const getters = {
  isFetching: state_ => state_.isFetching,
  animes: state_ => state_.data,
};

const actions = {
  getAnimes({ commit }, { page, size }) {
    const api = `/api/animes/?page=${page}&size=${size}`;
    axios.get(api)
    .then((rsp) => {
      const animeList = rsp.data.results;
      commit('listAnimes', animeList);
    });
  },
};

/* eslint-disable no-param-reassign */
const mutations = {
  listAnimes(state_, animeList) {
    state_.data = animeList;
  },
};
/* eslint-enable no-param-reassign */

export default {
  getters,
  state,
  actions,
  mutations,
};
