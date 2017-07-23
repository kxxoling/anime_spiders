<template lang="jade">
.video-list
  .list-container
    short-video.video(v-for="video in shortVideos", :video="video", key="video.id")
  el-pagination.pagination(
    layout="prev, pager, next",
    :page-count="pagesCount",
    @current-change="fetchPage"
  )
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import ShortVideo from '@/components/ShortVideo';

const PAGE_SIZE = 30;

export default {
  data() {
    return {
    };
  },
  mounted() {
    if (!this.shortVideos.length) {
      this.getVideos({ page: 1, size: PAGE_SIZE });
    }
  },
  computed: {
    ...mapGetters({
      shortVideos: 'shortVideos',
      isFetching: 'isFetching',
      pagesCount: 'videoPagesCount',
    }),
  },
  methods: {
    ...mapActions({
      getVideos: 'getVideos',
    }),
    fetchPage(val) {
      this.getVideos({ page: val, size: PAGE_SIZE });
    },
  },
  components: {
    ShortVideo,
  },
  metaInfo: {
    title: 'Short Videos',
  },
};
</script>

<style lang="stylus" scoped>
.video-list
  .video
    margin-bottom 1rem
</style>
