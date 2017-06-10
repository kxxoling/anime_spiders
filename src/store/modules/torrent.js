import axios from 'axios';

const state = {
  isFetching: false,
  data: [],
};

const getters = {
  isFetching: state_ => state_.isFetching,
  torrents: state_ => state_.data,
};

const actions = {
  getTorrents({ commit }, { page, size }) {
    const api = `/api/torrents/?page=${page}&size=${size}`;
    axios.get(api)
    .then((rsp) => {
      const torrentList = rsp.data.results;
      commit('listTorrents', torrentList);
    });
  },
};

/* eslint-disable no-param-reassign */
const mutations = {
  listTorrents(state_, torrentList) {
    state_.data = torrentList;
  },
};
/* eslint-enable no-param-reassign */

export default {
  getters,
  state,
  actions,
  mutations,
};
