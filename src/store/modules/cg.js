import axios from 'axios';

const state = {
  isFetching: false,
  data: [],
  pagesCount: null,
};

const getters = {
  isFetching: state_ => state_.isFetching,
  cgs: state_ => state_.data,
  cgPagesCount: state_ => state_.pagesCount,
};

const actions = {
  getCgs({ commit }, { page, size }) {
    const api = `/api/cgs/?page=${page}&size=${size}`;
    axios.get(api)
    .then((rsp) => {
      const cgList = rsp.data.results;
      commit('listCgs', cgList);
      commit('setPagesCount', rsp.data.pagesCount);
    });
  },
};

/* eslint-disable no-param-reassign */
const mutations = {
  listCgs(state_, cgList) {
    state_.data = cgList;
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
