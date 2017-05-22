import axios from 'axios';

const state = {
  isFetching: false,
  data: [],
};

const getters = {
  isFetching: state_ => state_.isFetching,
  cgs: state_ => state_.data,
};

const actions = {
  getCgs({ commit }, { page, size }) {
    const api = `/api/cgs/?page=${page}&size=${size}`;
    axios.get(api)
    .then((rsp) => {
      const cgList = rsp.data.results;
      commit('listCgs', cgList);
    });
  },
};

/* eslint-disable no-param-reassign */
const mutations = {
  listCgs(state_, cgList) {
    state_.data = cgList;
  },
};
/* eslint-enable no-param-reassign */

export default {
  getters,
  state,
  actions,
  mutations,
};
