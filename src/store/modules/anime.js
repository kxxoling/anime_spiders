import axios from 'axios';

const state = {
  isFetching: false,
  data: [],
  pagesCount: null,
};

const getters = {
  isFetchingAnimes: state_ => state_.isFetching,
  animes: state_ => state_.data,
  animePagesCount: state_ => state_.pagesCount,
};

const actions = {
  getAnimes({ commit }, { page, size }) {
    const api = `/api/animes/?page=${page}&size=${size}`;
    axios.get(api)
    .then((rsp) => {
      const animeList = rsp.data.results;
      const pagesCount = rsp.data.pagesCount;
      commit('listAnimes', animeList);
      commit('setPagesCount', pagesCount);
    });
  },
};

/* eslint-disable no-param-reassign */
const mutations = {
  listAnimes(state_, animeList) {
    state_.data = animeList;
  },
  setPagesCount(state_, pagesCount) {
    state_.pagesCount = pagesCount;
  },
};
/* eslint-enable no-param-reassign */

export default {
  getters,
  state,
  actions,
  mutations,
};
