import axios from 'axios';

const state = {
  isFetching: false,
  data: [],
};

const getters = {
  isFetching: state_ => state_.isFetching,
  shortVideos: state_ => state_.data,
};

const actions = {
  getVideos({ commit }, { page, size }) {
    const api = `/api/shortvideos/?page=${page}&size=${size}`;
    axios.get(api)
    .then((rsp) => {
      const videoList = rsp.data.results;
      commit('listVideos', videoList);
    });
  },
};

/* eslint-disable no-param-reassign */
const mutations = {
  listVideos(state_, videoList) {
    state_.data = videoList;
  },
};
/* eslint-enable no-param-reassign */

export default {
  getters,
  state,
  actions,
  mutations,
};
