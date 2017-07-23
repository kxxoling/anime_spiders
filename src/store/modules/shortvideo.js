import axios from 'axios';

const state = {
  isFetching: false,
  data: [],
  pagesCount: null,
};

const getters = {
  isFetchingVideos: state_ => state_.isFetching,
  shortVideos: state_ => state_.data,
  videoPagesCount: state_ => state_.pagesCount,
};

const actions = {
  getVideos({ commit }, { page, size }) {
    const api = `/api/shortvideos/?page=${page}&size=${size}`;
    axios.get(api)
    .then((rsp) => {
      const videoList = rsp.data.results;
      commit('listVideos', videoList);
      commit('setPagesCount', rsp.data.pagesCount);
    });
  },
};

/* eslint-disable no-param-reassign */
const mutations = {
  listVideos(state_, videoList) {
    state_.data = videoList;
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
