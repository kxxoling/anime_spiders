import axios from 'axios';

const state = {
  isFetching: false,
  data: [],
  pagesCount: null,
};

const getters = {
  isFetching: state_ => state_.isFetching,
  torrents: state_ => state_.data,
  torrentPagesCount: state_ => state_.pagesCount,
};

const actions = {
  getTorrents({ commit }, { page, size }) {
    const api = `/api/torrents/?page=${page}&size=${size}`;
    axios.get(api)
    .then((rsp) => {
      const torrentList = rsp.data.results;
      commit('listTorrents', torrentList);
      commit('setPagesCount', rsp.data.pagesCount);
    });
  },
};

/* eslint-disable no-param-reassign */
const mutations = {
  listTorrents(state_, torrentList) {
    state_.data = torrentList;
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
